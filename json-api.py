import requests
import json
import jsonpath

api_url = 'https://reqres.in/api/users?page=2'

# Make a request
response1 = requests.get(api_url)
print(response1.text)

# Validate Status Code
assert response1.status_code==200

# Parse response into JSON format
json_response = json.loads(response1.text)
print(json_response)

# Apply JSON Path (file, jsonpath)
y = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(y[0])

z = jsonpath.jsonpath(json_response, 'data[3].first_name')
print(z[0])

# Fetch all the first name in data
for val in json_response['data']:
    print(val['first_name'])