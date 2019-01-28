import requests


url = 'https://loremflickr.com/320/240' # https://httpbin.org/get # 'https://loremflickr.com/320/240', allow_redirects=True # https://jsonplaceholder.typicode.com/posts

response = requests.get(url, allow_redirects=True)

print(response)
print()
print(response.content)
print()
# print(response.json())
print()
# print(response.headers)
print()
# print(response.headers.get('Server'))
print()