import asyncio
import aiohttp
import uvloop
import time


# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def request(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			return await response.text()


async def main():
	start = time.time()
	url = 'http://httpbin.org/delay/3'
	await asyncio.gather(
		request(url),
		request(url),
		request(url),
		request(url),
		request(url),
	)
	print(time.time() - start)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())