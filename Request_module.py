import requests

# respose = requests.get("https://www.google.com")
# print(respose.text)



data = {
    "title": 'foo',
    "body": 'soo',
    "userId": 12,
    
}

headers = {
    'Content-type':'application/json;charset=UTF-8',
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",headers=headers, json=data)

print(response.text)