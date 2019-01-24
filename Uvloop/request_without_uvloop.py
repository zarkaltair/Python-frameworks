import requests


# Synchronous way
def request(url):
	return requests.get(url).text


def main():
	url = 'http://httpbin.org/delay/3'
	request(url)
	request(url)
	request(url)
	request(url)
	request(url)


if __name__ == '__main__':
	main()