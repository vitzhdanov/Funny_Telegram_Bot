import requests
from aiogram.utils.markdown import hitalic, hbold, hunderline


def phrase_day():
    req = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json').json()
    phrase = f"{hunderline('Цитата дня')}\n{hitalic(req['quoteText'])}\n{hbold(req['quoteAuthor'])}"
    return phrase
