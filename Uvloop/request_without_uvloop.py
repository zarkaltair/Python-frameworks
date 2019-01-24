import requests
import time


# Synchronous way
def request(url):
	return requests.get(url).text


def main():
	start = time.time()
	url = 'http://httpbin.org/delay/3'
	request(url)
	request(url)
	request(url)
	request(url)
	request(url)
	print(time.time() - start)


if __name__ == '__main__':
	main()