import requests
import xmltodict
import json


# Каждый день запрашивает гороскоп и хранит его в json
async def horoscope():
    general = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml').text
    erotic = requests.get('https://ignio.com/r/export/utf/xml/daily/ero.xml').text
    business = requests.get('https://ignio.com/r/export/utf/xml/daily/bus.xml').text
    health = requests.get('https://ignio.com/r/export/utf/xml/daily/hea.xml').text
    cooking = requests.get('https://ignio.com/r/export/utf/xml/daily/cook.xml').text
    love = requests.get('https://ignio.com/r/export/utf/xml/daily/lov.xml').text

    with open('utils/horoscopes/general.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(general), f, ensure_ascii=False, indent=4)
    with open('utils/horoscopes/erotic.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(erotic), f, ensure_ascii=False, indent=4)
    with open('utils/horoscopes/business.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(business), f, ensure_ascii=False, indent=4)
    with open('utils/horoscopes/health.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(health), f, ensure_ascii=False, indent=4)
    with open('utils/horoscopes/cooking.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(cooking), f, ensure_ascii=False, indent=4)
    with open('utils/horoscopes/love.json', 'w', encoding='utf-8') as f:
        json.dump(xmltodict.parse(love), f, ensure_ascii=False, indent=4)