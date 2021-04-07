import requests
from requests import HTTPError
import json


response = requests.get('https://jsonplaceholder.typicode.com/posts')
json_data = json.dumps(response.json(), indent=2)

print(json_data)
print(type(json_data))

