import json
import sys
import datetime
import sqlite3
conn = sqlite3.connect('pogoda.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS pogoda(
            city_id integer primary key,
            city varchar(255),
            nasha_data DATE,
            temperature integer,
            weather_id integer 
            )''')

def time_converter(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')
    return converted_time


def get_city(vvod):
    a = {}
    city = vvod[0]
    country = vvod[1]
    with open('city_list.json', 'r', encoding='utf-8') as fh:
        cities = json.load(fh)
    for item in cities:
        if city in item.values() and country in item.values():
            a = item
    return a['id']


def get_data(city_id):
    import urllib.request
    with open('app.id', 'r') as f:
        api_id = f.read()
    url = 'http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}'.format(str(city_id), str(api_id))
    data_forecast = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))

    return data_forecast



def data_organizer(raw_api_dict):
    data = dict(
        city=raw_api_dict.get('name'),
        country=raw_api_dict.get('sys').get('country'),
        temp=raw_api_dict.get('main').get('temp'),
        temp_max=raw_api_dict.get('main').get('temp_max'),
        temp_min=raw_api_dict.get('main').get('temp_min'),
        humidity=raw_api_dict.get('main').get('humidity'),
        pressure=raw_api_dict.get('main').get('pressure'),
        sky=raw_api_dict['weather'][0]['main'],
        sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
        sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
        wind=raw_api_dict.get('wind').get('speed'),
        wind_deg=raw_api_dict.get('deg'),
        dt=time_converter(raw_api_dict.get('dt')),
        cloudiness=raw_api_dict.get('clouds').get('all')
    )
    return data


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print('Current weather in: {}, {}:'.format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print('Max: {}, Min: {}'.format(data['temp_max'], data['temp_min']))
    print('')
    print('Wind Speed: {}, Degree: {}'.format(data['wind'], data['wind_deg']))
    print('Humidity: {}'.format(data['humidity']))
    print('Cloud: {}'.format(data['cloudiness']))
    print('Pressure: {}'.format(data['pressure']))
    print('Sunrise at: {}'.format(data['sunrise']))
    print('Sunset at: {}'.format(data['sunset']))
    print('')
    print('Last update from the server: {}'.format(data['dt']))
    print('---------------------------------------')
vvod = input('Введите название города на английском и 2 буквы страны ').split(' ')
data_output(data_organizer(get_data(get_city(vvod))))