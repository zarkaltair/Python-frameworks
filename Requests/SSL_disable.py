import requests


# отключение SSL
url = 'https://free-proxy-list.net/'
response = requests.get(url, verify=False)
print(response)