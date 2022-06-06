''' Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.'''


duration = int(input('Введите количество секунд: '))

days = int
if duration // 86400 >= 1:
    days  = duration//86400
else:
    days = 0

hours = int
if duration //3600>=1:
    hours = (duration - (days * 86400))//3600
else:
    hours = 0

minutes = int
if duration // 60 >=1:
    minutes = (duration - (days * 86400 + hours * 3600)) // 60
else:
    minutes = 0

seconds = duration - (days*86400 + hours*3600 + minutes*60)

if days == 0 and hours == 0 and minutes == 0:
    print (seconds, 'сек')
elif days == 0 and hours == 0 and minutes > 0:
    print(minutes, 'мин', seconds, 'сек')
elif days == 0 and hours > 0:
    print(hours, 'ч', minutes, 'мин', seconds, 'сек')
else:
    print(days, 'дн', hours, 'ч', minutes, 'мин', seconds, 'сек')


one_to_thousand = list(range(1, 1000, 2))
cubes = []
order = []
sums_of_divisible = 0
n = 0
for i in one_to_thousand:
    cubes.append(i**3)
for i in cubes:
    n = i
    while i > 0:
        order.append(i%10)
        i //= 10
    if sum(order) % 7 == 0:
        sums_of_divisible += n
    n = 0
    order.clear()
print(sums_of_divisible)


'''Реализовать склонение слова «процент» во фразе «N процентов».
 Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
'''
ending = str
n = 1
while n<101:
    if n == 1 or n % 10 == 1 and n != 11:
        ending = ''
    elif (n != 12 and n != 13 and n != 14) and (n % 10 == 2 or n % 10 == 3 or n % 10 == 4):
        ending = 'а'
    else:
        ending = 'ов'
    print (n, 'процент'+ending)
    n += 1
