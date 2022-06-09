# Задание №1

dictionary = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate():
    eng = input('Введите цифру на английском: ')

    translate = dictionary.get(eng)
    return translate


print(num_translate())


# Задание №3


def thesaurus(*args):
    employees = {}
    for i in args:
        if i[0] not in employees:
            employees[i[0]] = [i]
        else:
            employees[i[0]].append(i)
    return employees

print(thesaurus("маша", "ваня", "петя","марина", "петр"))

# Задание №5

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []

def get_jokes(n):
    while n > 0:
        jokes.append(f'{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} {adjectives[randrange(len(adjectives))]}')
        n -=1
    return jokes

print (get_jokes(5))