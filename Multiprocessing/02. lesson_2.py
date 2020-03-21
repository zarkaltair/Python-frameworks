from multiprocessing.pool import ThreadPool
import requests
from datetime import datetime


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


if __name__ == "__main__":
    print(parallel_extraction(16, 64))
