import requests

headers = {'Content-type': 'application/json'}
request=requests.put('http://127.0.0.1:5002/user_info', json={"user": "v", "password": "ddd"}, headers=headers)
print(request.json())