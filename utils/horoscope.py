import requests
from bs4 import BeautifulSoup
import xmltodict, json


async def horoscope():
    general = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml').text
    erotic = requests.get('https://ignio.com/r/export/utf/xml/daily/ero.xml').text
    business = requests.get('https://ignio.com/r/export/utf/xml/daily/bus.xml').text
    health = requests.get('https://ignio.com/r/export/utf/xml/daily/hea.xml').text
    cooking = requests.get('https://ignio.com/r/export/utf/xml/daily/cook.xml').text
    love = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml').text

    with open('general.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(general), f, ensure_ascii=False, indent=4)
    with open('erotic.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(erotic), f, ensure_ascii=False, indent=4)
    with open('business.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(business), f, ensure_ascii=False, indent=4)
    with open('health.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(health), f, ensure_ascii=False, indent=4)
    with open('cooking.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(cooking), f, ensure_ascii=False, indent=4)
    with open('love.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(love), f, ensure_ascii=False, indent=4)

