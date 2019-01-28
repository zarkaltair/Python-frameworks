import requests


url = 'https://jsonplaceholder.typicode.com/posts' # https://httpbin.org/get

response = requests.get(url)

print(response)
print()
# print(response.content)
print()
print(response.json())
print()
# print(response.headers)
print()
# print(response.headers.get('Server'))
print()