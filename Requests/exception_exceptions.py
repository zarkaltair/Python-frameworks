import requests


# Exception Connect Timeout
try:
    response = requests.get('https://httpbin.org/user-agent', timeout=(0.00001, 10))
except requests.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')
   
# Exception Read Timeout
try:
    response = requests.get('https://httpbin.org/user-agent', timeout=(10, 0.0001))
except requests.exceptions.ReadTimeout:
    print('Oops. Read timeout occured!')
except requests.exceptions.ConnectTimeout:
    print('Oops. Connection timeout occured!')

# Exception Connection Error
try:
    response = requests.get('http://urldoesnotexistforsure.bom')
except requests.exceptions.ConnectionError:
    print('Seems like DNS lookup failed...')

# Exception HTTP Error
try:
    response = requests.get('https://httpbin.org/status/500')
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Oops. HTTP Error occured!')
    print('Response is: {content}'.format(content=err.response.content))