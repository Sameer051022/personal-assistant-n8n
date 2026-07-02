import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/add2d85f-1d08-4c6e-a833-dfee9b004cfb"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])