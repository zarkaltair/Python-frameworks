import requests


# check internet connection
def internetConnection():
	try:
		requests.get('http://google.com', timeout=3)
		print('connected')
	except requests.exceptions.ConnectionError:
		print('not connected')
		
internetConnection()