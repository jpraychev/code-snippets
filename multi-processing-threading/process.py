from concurrent.futures import ProcessPoolExecutor
import requests
import time

def fetch(url):
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    
    URL = 'https://httpbin.org/uuid'
    t0 = time.time()
    
    with ProcessPoolExecutor() as executor:
        executor.map(fetch, [URL for _ in range(50)])
    
    print(f'It took {time.time() - t0:.2f} secs to finish multiprocessing')