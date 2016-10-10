import json


def load_data(filepath):
    data = None
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data


def get_biggest_bar(data):
    return max(data, key = lambda x: x['Cells']['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key = lambda x: x['Cells']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    return min(
        (deviation(longitude, latitude, bar_data) 
        for bar_data in data),
        key = lambda x: x['deviation']
    )['bar']


def deviation(longitude, latitude, bar_data):
    x = abs(longitude - bar_data['Cells']['geoData']['coordinates'][0])
    y = abs(latitude - bar_data['Cells']['geoData']['coordinates'][1])
    return {'deviation':x + y, 'bar':bar_data}
    

def show_bar_information(bar_data):
    bar = bar_data['Cells']
    print('Название: {0}'.format(bar['Name']))
    print('Административный округ: {0}'.format(bar['AdmArea']))
    print('Район: {0}'.format(bar['District']))
    print('Адрес: {0}'.format(bar['Address']))
    print('Телефон: {0}'.format(bar['PublicPhone'][0]['PublicPhone']))
    print('Количество мест: {0}'.format(bar['SeatsCount']))
    print('Долгота: {0}; Широта: {1}'.format(
        bar['geoData']['coordinates'][0],
        bar['geoData']['coordinates'][1]
    ))


if __name__ == '__main__':
    data = load_data(input('Введите имя файла с данными о барах: '))
    print('\nСАМЫЙ БОЛЬШОЙ БАР\n')
    show_bar_information(get_biggest_bar(data))
    print('\nСАМЫЙ МАЛЕНЬКИЙ БАР\n')
    show_bar_information(get_smallest_bar(data))
    print('\nБЛИЖАЙШИЙ БАР\n')
    show_bar_information(get_closest_bar(data,
        float(input('Введите долготу: ')),
        float(input('Введите широту: '))
    ))
