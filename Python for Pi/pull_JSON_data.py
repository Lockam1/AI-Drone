import requests

x = requests.get('http://localhost:8080/')
print(x.status_code)
print()
