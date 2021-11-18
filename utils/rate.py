from aiogram.utils.markdown import hbold
from bs4 import BeautifulSoup as bs

import requests

from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rate = ['https://mainfin.ru/currency/usd','https://mainfin.ru/currency/eur','https://mainfin.ru/crypto/bitcoin']
result = []


def exchange_rate(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    for i in url:
        if 'crypto' in i:
            url1 = requests.get(f'{i}', headers).text
            soup1 = bs(url1, 'lxml')
            res1 = soup1.find('div', class_="crypto_curr_val").text
            result.append(res1.replace('$', '').replace(' ', ''))
        else:
            url = requests.get(f'{i}', headers).text
            soup = bs(url, 'lxml')
            res = soup.find('td', class_="mark-text").text
            result.append(res)


exchange_rate(rate)

data = CallbackData('chose', 'rates')
usd = f'USD - {result[0]} ₽'
eur = f'EUR - {result[1]} ₽'
btc = f'BTC - {result[2]} 💲'

key = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=btc, callback_data=data.new(rates='btc'))
    ],
    [
        InlineKeyboardButton(text=usd, callback_data=data.new(rates='usd'))
    ],
    [
        InlineKeyboardButton(text=eur, callback_data=data.new(rates='eur'))
    ]
])