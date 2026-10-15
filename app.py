
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "course": "AI/ML", "marks": 85},
    {"id": 2, "name": "Priya", "course": "Data Science", "marks": 91}
]


# Shared function to create a student
def create_student(data):
    if not isinstance(data, dict):
        return None, "Invalid student data"

    name = data.get("name")
    course = data.get("course")
    marks = data.get("marks")

    if not isinstance(name, str) or not name.strip():
        return None, "Valid student name is required"

    if not isinstance(course, str) or not course.strip():
        return None, "Valid course is required"

    if isinstance(marks, bool):
        return None, "Marks must be a number between 0 and 100"

    try:
        marks = float(marks)
    except (TypeError, ValueError):
        return None, "Marks must be a number between 0 and 100"

    if not 0 <= marks <= 100:
        return None, "Marks must be between 0 and 100"

    if marks.is_integer():
        marks = int(marks)

    student = {
        "id": max((s["id"] for s in students), default=0) + 1,
        "name": name.strip(),
        "course": course.strip(),
        "marks": marks
    }

    students.append(student)
    return student, None


# Home page
@app.route("/")
def home():
    return render_template("index.html", students=students)


# API: Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


# API: Get one student
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student), 200


# API: Add student using JSON
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)
    student, error = create_student(data)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(student), 201


# API: Update student using JSON
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return jsonify({"error": "Valid JSON data is required"}), 400

    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    updated = {
        "name": data.get("name", student["name"]),
        "course": data.get("course", student["course"]),
        "marks": data.get("marks", student["marks"])
    }

    # Validate before changing the existing student
    candidate, error = validate_student_data(updated)

    if error:
        return jsonify({"error": error}), 400

    student.update(candidate)
    return jsonify(student), 200


def validate_student_data(data):
    if not isinstance(data.get("name"), str) or not data["name"].strip():
        return None, "Valid student name is required"

    if not isinstance(data.get("course"), str) or not data["course"].strip():
        return None, "Valid course is required"

    marks = data.get("marks")

    if isinstance(marks, bool):
        return None, "Marks must be a number between 0 and 100"

    try:
        marks = float(marks)
    except (TypeError, ValueError):
        return None, "Marks must be a number between 0 and 100"

    if not 0 <= marks <= 100:
        return None, "Marks must be between 0 and 100"

    if marks.is_integer():
        marks = int(marks)

    return {
        "name": data["name"].strip(),
        "course": data["course"].strip(),
        "marks": marks
    }, None


# API: Delete student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    students.remove(student)
    return jsonify({"message": "Student deleted successfully"}), 200


# HTML form: Add student
@app.route("/add-student", methods=["POST"])
def add_student_from_form():
    student, error = create_student({
        "name": request.form.get("name"),
        "course": request.form.get("course"),
        "marks": request.form.get("marks")
    })

    if error:
        return error, 400

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)