# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

# def minimum(arr):
#     pass

# def maximum(arr):
#     pass

# Решение

import random
base0 = list(range(-20, 20, 2))
a = random.choices(base0, k=10)
print("Произвольный список: ", a)
def minimum(arr):
    arr.sort()  
    m = arr[0]
    return m
def maximum(arr):
    arr.sort()  
    b = arr[-1]
    return b
minimum(a)
maximum(a)
print('min=', minimum(a), ', max=', maximum(a))