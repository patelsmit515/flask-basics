# Student Management API

A beginner-friendly Student Management application built with **Python and Flask**. This project demonstrates basic REST API development, HTTP methods, request handling, input validation, and HTML form integration.

## Features

* View all students and retrieve individual student records.
* Add students using a JSON API or HTML form.
* Update student details.
* Delete student records.
* Validate input data and handle errors using HTTP status codes.
* Display student information using Flask templates and Jinja.

## Technologies Used

* Python
* Flask
* HTML
* Jinja Templates
* Requests (for API testing)

## Project Structure
student_managment_api/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── test_api.py
├── test_update.py
├── test_delete.py
└── README.md


## Installation and Setup

1. Clone this repository:

   
   git clone YOUR_GITHUB_REPOSITORY_URL


2. Navigate to the project folder:


   cd student_managment_api


3. Install the dependencies:


   pip install -r requirements.txt


4. Run the application:


   python app.py


5. Open the application in your browser:

   `http://127.0.0.1:5000/`

## API Endpoints

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/students`              | Retrieve all students      |
| GET    | `/students/<student_id>` | Retrieve a student by ID   |
| POST   | `/students`              | Add a student using JSON   |
| PUT    | `/students/<student_id>` | Update a student's details |
| DELETE | `/students/<student_id>` | Delete a student           |

### Example: Add a Student

Send a POST request to `/students` with a JSON body:

{
    "name": "Amit",
    "course": "Python",
    "marks": 88
}

The API returns the created student with HTTP status code `201 Created`.

## Testing

Start the Flask server first, then run the test scripts in separate terminal commands:

python test_api.py
python test_update.py
python test_delete.py


You can also test the API using tools such as Postman.

## Limitations

Student records are stored in an in-memory Python list. The data resets when the application restarts. A database can be added in a future version for persistent storage.

## Learning Objectives

This project helped me practise Flask routing, REST API development, HTTP methods, JSON handling, HTML forms, template rendering, input validation, and error handling.

## Future Improvements

* Integrate a database such as SQLite.
* Add automated tests using pytest.
* Improve the user interface and error messages.