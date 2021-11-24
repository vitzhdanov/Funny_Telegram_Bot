import requests

print(requests.post('https://www.iclc.info/shortner/', {'long_url': 'https://realpython.com/courses/reading-input-writing-output-python/'}).json()['short_sym'])