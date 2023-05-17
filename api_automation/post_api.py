import json

import jsonpath as jsonpath
import requests

# API URL
url = "https://reqres.in/api/users"

# Read Input JSON file
file = open(
    "C:\\Personal_Code\\DSA_Solution_Python\\api_automation\\post_api.json", "r"
)

# Read the file content
json_input = file.read()

# Convert the string to JSON format
request_json = json.loads(json_input)

# Make POST request with JSON input body
response = requests.post(url, request_json)

# Validating Response Code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers)

# Parse response to JSON format
response_json = json.loads(response.text)

# Pick ID using JSON Path

id = jsonpath.jsonpath(response_json, "id")
print("id is", id[0])
