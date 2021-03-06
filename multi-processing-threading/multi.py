import requests
import time

URL = 'https://httpbin.org/uuid'

t0 = time.time()

for _ in range(50):
    response = requests.get(URL)
    return response.json()

print(f'It took {time.time() - t0:.2f} s to finish the request')