# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# def switch_it_up(number):
#     pass

# Решение
opis_cifr = {
    0: 'ноль',
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'чертыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять'
}
x = int
def switch_it_up(number):
    number = int(input('Введите цифру:'))
    return number
print(opis_cifr.get(switch_it_up(x)))