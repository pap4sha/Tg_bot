import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


def get_first_news():
    # Назначение юзер агента и юрл адреса digital для парсинга
    headers = {'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Mobile Safari/537.36'}
    url = 'https://digital.tatarstan.ru/index.htm/news/tape'
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all(class_="field-content")

    print (r)