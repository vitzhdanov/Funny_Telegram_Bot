import datetime

import requests
from aiogram import types
from aiogram.utils.markdown import hunderline, hbold
from loader import dp



response = requests.get('https://yesno.wtf/api').json()['image']
print(response)