import requests


def test(command, user=None, password=None):
    url = 'http://127.0.0.1:5002/user_info'
    headers = {'Content-type': 'application/json'}
    json = {}
    if user!=None:
        json.update({'user': user})
    if password!=None:
        json.update({'password': password})
    
    if command == 'post':
        request=requests.post(url, json=json, headers=headers)
    elif command == 'put':
        request=requests.put(url, json=json, headers=headers)
    elif command == 'delete':
        request=requests.delete(url, json=json, headers=headers)
    else: 
        print("Wrong command")
    print("command: {}, user: {}, password: {}".format(command,user,password))
    print(request.json())

test('post', 'post_user', 'post_pass')
test('post', None, 'post_pass2')
test('post', 'post_user2', None)
test('put', 'put_user', 'put_pass')
test('put', None, 'put_pass2')
test('put', 'put_user2', None)
test('delete', 'delete_user', 'delete_pass')
test('delete', None, 'delete_pass2')
test('delete', 'delete_user2', None)