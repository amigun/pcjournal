from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

SUBJECTS = [
    'Иностранный язык',
    'ДОП',
    'Физическая культура',
    'Элементы высшей математики',
    'Архитектура аппаратных средств',
    'Основы алгоритмизации и программирования',
    'МДК.04.01',
    'Стандартизация, сертификация и техническое документоведение',
    'Психология общения',
    'Менеджмент в профессиональной деятельности'
]


def get_date_by_weekday(weekday: str):
    weekdays = {
        'Понедельник': 0,
        'Вторник': 1,
        'Среда': 2,
        'Четверг': 3,
        'Пятница': 4,
        'Суббота': 5,
    }

    return (datetime.now() - timedelta(days=datetime.now().weekday()) + timedelta(days=weekdays.get(weekday))).strftime(
        '%Y-%m-%d')


def get():
    raw = requests.get('https://oksei.ru/studentu/raspisanie_uchebnykh_zanyatij?group=2пк2').text
    soup = BeautifulSoup(raw, features='html.parser')

    schedule = {}

    table = soup.find('table', attrs={'class': 'table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        weekday = row.find('th').text
        ol = row.find('td').find('ol')

        lis = []
        for li in ol.find_all('li'):
            for subject in SUBJECTS:
                if (li.text).startswith(subject):
                    lis.append(subject)

        schedule[weekday] = [get_date_by_weekday(weekday), lis]

    return schedule
