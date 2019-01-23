import requests


response = requests.get('https://httpbin.org/get')
print(response.content)
print()
print(response.json())
print()
print(response.headers)
print()
print(response.headers.get('Server'))
print()