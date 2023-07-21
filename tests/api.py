import requests

def login_user(base_url, username, password, code, uuid):
    url = f"{base_url}/prod-api/login"
    data = {
        "username": username,
        "password": password,
        "code": code,
        "uuid": uuid
    }
    response = requests.post(url, json=data)
    return response
