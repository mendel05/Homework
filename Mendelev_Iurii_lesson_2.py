# Задание №1

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

# Задание №2
task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

task_list_new = []
for i in task_list:
    for j in i:
        if j.isdigit() == 0 and j != '+':
            task_list_new.append(i)
            break
        elif j.isdigit() == 1:
            task_list_new.append('"')
            task_list_new.append(f'{int(i):02d}')
            task_list_new.append('"')
            break
print (task_list_new)

result = ' '.join(task_list_new)
print (result)

# Задание №4
employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in employees:
    j = i.split()
    print (f'Привет, {j[-1].capitalize()}')

# Задание №5
prices = [57.8, 46.51, 97, 65, 78.2, 51.87, 894.6, 651.51, 17.69, 51.08, 8.65, 95]

for i in prices:
    print(f'{i:.2f}', end=', ')
print ('id =', id(prices))

prices.sort()
for i in prices:
    print(f'{i:.2f}', end=', ')
print('id =', id(prices))

new_prices = sorted(prices, reverse=True)
print(new_prices)
print(prices[-1:-6:-1])