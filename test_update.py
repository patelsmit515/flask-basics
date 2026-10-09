
import requests

url = "http://127.0.0.1:5000/students/1"

updated_data = {
    "marks": 95
}

response = requests.put(url, json=updated_data)

print("Status:", response.status_code)
print("Response:", response.json())