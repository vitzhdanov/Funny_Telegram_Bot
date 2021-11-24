import requests

print(requests.post('https://www.iclc.info/shortner/', {'long_url': 'https://www.youtube.com/watch?v=5qJ_wjQLFiQ&ab_channel=Jazz%26BossaCollection'}).json()['short_sym'])