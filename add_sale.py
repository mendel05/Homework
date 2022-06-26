put = input("Введите сумму продаж: ")


with open ('bakery.csv', 'a', encoding='utf-8') as bakery:
    bakery.write(put + '\n')

