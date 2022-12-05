# How To Get Data From REST API With Python:
# Getting data from external REST APIs is a common task when programming in Python. 
# In this short tutorial you’ll learn the fastest and easiest way to read data from 
# a REST API by using the Python programming language. 

import requests
import json



api_response = requests.get('https://jsonplaceholder.typicode.com/todos')
print(api_response.status_code)
data = api_response.text
parse_json = json.loads(data)

print("Todos:", parse_json)