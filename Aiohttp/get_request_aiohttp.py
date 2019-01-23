import requests


def hello():
	return requests.get('http://httpbin.org/get')

print(hello())



import asyncio

from aiohttp import ClientSession


async def hello(url):
	async with ClientSession() as session:
		async with session.get(url) as response:
			response = await response.read()
			print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello('http://httpbin.org/headers'))