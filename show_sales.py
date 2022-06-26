put = input('Введите диапазон: ')

if len(list(put.split())) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        cont = bakery.readlines()
        print(cont[int(put.split()[0]) - 1:int(put.split()[1])])
elif len(list(put.split())) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        cont = bakery.readlines()
        print(cont[int(put.split()[0]) - 1:])
else:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        cont = bakery.readlines()
        print(cont)