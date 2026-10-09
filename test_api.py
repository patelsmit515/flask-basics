import requests

url = "http://127.0.0.1:5000/students"

student = {
    "name": "Amit",
    "course": "Python",
    "marks": 88
}

response = requests.post(url, json=student)

print("Status:", response.status_code)
print("Response:", response.json())