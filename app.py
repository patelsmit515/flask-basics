from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Rahul",
        "course": "AI/ML",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Priya",
        "course": "Data Science",
        "marks": 91
    }
]

@app.route("/")
def home():
    return render_template("index.html", students=students)


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def add_student():
    new_student = request.get_json()

    if not new_student or "name" not in new_student:
        return jsonify({"error": "Student name is required"}), 400

    new_student["id"] = max(
        (student["id"] for student in students),
        default=0
    ) + 1

    students.append(new_student)

    return jsonify(new_student), 201


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "Request data is required"}), 400

    for student in students:
        if student["id"] == student_id:
            for key in ["name", "course", "marks"]:
                if key in updated_data:
                    student[key] = updated_data[key]

            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({
                "message": "Student deleted successfully"
            }), 200

    return jsonify({"error": "Student not found"}), 404


@app.route("/add-student", methods=["POST"])
def add_student_from_form():
    name = request.form.get("name")
    course = request.form.get("course")
    marks = request.form.get("marks")

    if not name or not course or not marks:
        return "All fields are required", 400

    new_student = {
        "id": max(
            (student["id"] for student in students),
            default=0
        ) + 1,
        "name": name,
        "course": course,
        "marks": int(marks)
    }

    students.append(new_student)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

