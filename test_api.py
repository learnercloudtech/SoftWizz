import requests

url = "http://127.0.0.1:8000/query"
payload = {
    "prompt": "Show all employees in HR"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Raw Response Text:", response.text)  # 👈 see what server actually returns

try:
    print("Parsed JSON:", response.json())  # only try if valid JSON
except Exception as e:
    print("JSON Parse Error:", str(e))
