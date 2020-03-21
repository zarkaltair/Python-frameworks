from datetime import datetime
from multiprocessing.pool import ThreadPool
from itertools import chain
import pandas as pd
import requests
import aiohttp
import asyncio


URL = "https://medium.fabianbosler.de/run"

def fetch_quote(*args):
    try:
        res = requests.get(URL).json()
    except Exception:
        res = 'ERROR'
    return res

def parallel_extraction(threads, samples):
    start = datetime.now()
    res = []
    with ThreadPool(processes=threads) as pool:
        res.extend(pool.map(fetch_quote, range(samples)))

    return res, datetime.now() - start

def sequential_extraction(samples):
    start = datetime.now()
    res = []
    for dt in range(samples):
        res.append(fetch_quote())
    return res, datetime.now() - start

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
    benchmarking_res = []

    for num_samples in chain(range(0, 10, 3), range(10, 20, 5), [50], range(100, 2100, 600)):
        for num_threads in [-1, 0, 8, 16, 24, 32, 64, 128]:
            print(f'started with {num_samples} samples and {num_threads} threads')
            if num_threads == -1:
                data, time = asyncio.run(sample_asyncio(num_samples))
            elif num_threads == 0:
                data, time = sequential_extraction(num_samples)
            else:
                data, time = parallel_extraction(num_threads, num_samples)
            errors = len([x for x in data if x == 'ERROR'])

            benchmarking_res.append({
                'num_samples': num_samples,
                'num_threads': num_threads,
                'execution_time': time,
                'errors': errors
            })

    _ = pd.DataFrame(benchmarking_res)
    _.to_csv('results.csv', index=False)
    _ = pd.pivot(_, index='num_samples', columns='num_threads', values='execution_time')
    _.applymap(lambda x: pd.to_timedelta(x)).plot(figsize=(16, 9))
