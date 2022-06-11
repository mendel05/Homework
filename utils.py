import requests


def currency_rates(char_code):
    r = requests.post('http://www.cbr.ru/scripts/XML_daily.asp')
    link = r.text.split('><CharCode>')

    my_dict = {}
    for i in link:
        my_dict[i[0:3]] = i[-65:-59]
    return f'1 {char_code} = {my_dict[char_code]} рублей'

if __name__ == '__main__':
    currency_rates()