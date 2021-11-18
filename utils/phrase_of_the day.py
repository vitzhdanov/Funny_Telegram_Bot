import requests

req = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&format=json').json()
phrase = f"{req['quoteText']}\n{req['quoteAuthor']}"
