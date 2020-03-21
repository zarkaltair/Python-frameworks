from datetime import datetime
import aiohttp
import asyncio

URL = "https://medium.fabianbosler.de/run"

async def sample_asyncio(samples):
    async def main():
        results = []
        async with aiohttp.ClientSession() as session:
            for i in range(samples):
                async with session.get(URL) as resp:
                    results.append(await resp.json())
        return results

    start = datetime.now()
    return await main(), datetime.now()-start


if __name__ == '__main__':
    print(asyncio.run(sample_asyncio(64)))
