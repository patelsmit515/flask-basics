# Student Management API

A beginner-friendly Student Management application built with **Python, Flask, and Docker**. This project demonstrates REST API development, HTTP methods, input validation, HTML form handling, and application containerization.

## Features

- View all students and retrieve individual records.
- Add students through a JSON API or HTML form.
- Update and delete student records.
- Validate input and handle errors using HTTP status codes.
- Render student information using Flask templates and Jinja.
- Build and run the application inside a Docker container.

## Technologies Used

- Python
- Flask
- HTML and Jinja Templates
- Docker
- Requests (API testing)

## Project Structure

```text
student_managment_api/
├── app.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── templates/
│   └── index.html
├── test_api.py
├── test_update.py
├── test_delete.py
└── README.md
```

## Installation and Setup

### Option 1: Run Locally

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd student_managment_api
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open the application:

   http://127.0.0.1:5000/

### Option 2: Run with Docker

Make sure Docker Desktop is running and open a terminal in the project directory.

1. Build the Docker image:

   ```bash
   docker build -t student.api .
   ```

2. Create and start a container:

   ```bash
   docker run -d --name student-container -p 5000:5000 student.api
   ```

3. Open the application:

   http://localhost:5000/

#### Useful Docker Commands

| Command | Purpose |
|---|---|
| `docker images` | List Docker images |
| `docker ps` | View running containers |
| `docker ps -a` | View all containers |
| `docker logs student-container` | View application logs |
| `docker stop student-container` | Stop the application |
| `docker start student-container` | Start the container again |
| `docker rm student-container` | Remove a stopped container |

To rebuild the image after changing the application code, build the image again and recreate the container.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| GET | `/students/<student_id>` | Retrieve a student by ID |
| POST | `/students` | Add a student using JSON |
| PUT | `/students/<student_id>` | Update a student's details |
| DELETE | `/students/<student_id>` | Delete a student |

### Example: Add a Student

Send a POST request to `/students` with a JSON body:

```json
{
    "name": "Amit",
    "course": "Python",
    "marks": 88
}
```

A successful request returns the created student with HTTP status code `201 Created`.

## Testing

Start the application first, then run the test scripts in separate terminal commands:

```bash
python test_api.py
python test_update.py
python test_delete.py
```

You can also test the API using Postman.

## Limitations

- Student records are stored in an in-memory Python list and reset when the application restarts.
- The application is intended for learning and is not configured for production deployment.
- Docker packages the application and its dependencies but does not add persistent data storage.

## Learning Objectives

This project provided practical experience with Flask routing, REST APIs, HTTP methods, JSON handling, HTML forms, Jinja templates, input validation, error handling, Docker images, containers, port mapping, and container management.

## Future Improvements

- Add a database such as SQLite for persistent storage.
- Write automated tests using pytest.
- Improve the user interface and error messages.
- Explore Docker Compose and production deployment.