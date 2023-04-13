# spisok = [2, 13, 5, 7, 11, 13]
# spisok4 = ['a', 'b', 'v', 'g', 'd']
# stroka = '2, 3, 5, 7, 11, 13'
# matrica = [ [4,5] , [7,9] ]
# print(spisok[-1])
# string = '2, 3, 5, 7, 11, 13'
# chars = list(string)
# print(chars)
# print(spisok[::-1])
# print(len(spisok))
# spisok.append(15)
# a = [50, 60]
# # print(spisok)
# b = '2slovo'
# spisok.extend(b)
# print(stroka)
# spisok.append(b)
# spisok.extend(a)
# spisok.extend(c)
# spisok.insert(0, a)
# spisok[-2] = 20
# spisok.remove(2)
# del spisok[1:3]
# del stroka[1:3]
# spisok2 = spisok
# spisok3 = spisok * 3
# stroka *= 2
# print('id spisok:  ', id(spisok))
# print('id spisok2: ', id(spisok2))
# print('id spisok3: ', id(spisok3))
# print('spisok3: ', spisok3)
# print('spisok3 is spisok: ', spisok3 is spisok[:])
# print('spisok3 == spisok: ', spisok3 == spisok[:])
# print('spisok2 is spisok: ', spisok2 is spisok)
# print('spisok2 == spisok: ', spisok2 == spisok)
# print(list('abcdefg'))
# print(list(range(5, 160, 10)))
# print(list(range(0, 5)))
# print(spisok == [4, 3, 5, 7, 11, 13])
# x = (1, 2, 3, 4, 5)
# print(list(x))
# '::'.join(spisok4)
# print('::'.join(spisok4))
# import copy
# spisok5 = copy.deepcopy(spisok3)
# print('spisok5 is spisok3: ', spisok5 is spisok3)
# print('spisok5 == spisok3: ', spisok5 == spisok3)
# print('id(spisok5): ', id(spisok5)) 
# print('id(spisok3): ', id(spisok3))
# print(spisok5 is spisok3)
# print(spisok5 == spisok3)
# print(id(spisok5)) 
# print(id(spisok3))
# print(spisok5 is spisok)
# dog_name = 'Жужа'
# pet_name = dog_name.replace('Ж', 'П')
# print('', dog_name,'\n',pet_name)
# a = 5
# b = 8
# a, b = b, a
# print('a: ', a, ';  b: ', b)
# vocabulary = { 'а' : ('ананас', 'апельсин', 'арбуз'),
# 'б' : ('баклажан','батат', 'брюква') }
# book = vocabulary
# book['в'] = ('виноград')
# print(vocabulary,'\n',book)
# # print(vocabulary.get('Италия', 'Отсутствует'))
# vocabulary.setdefault('Италия')
# C = {10, 20, 30, 40}
# D = C
# D.update({50, 60})
# print(C,'\n',D)
# movie_list = ['Челюсти', 'Касабланка', 'Оно']
# if movie_list:
#     print('Успех')
# x = -1
# print('Здравствуйте!')
# if x < 0:
#     print('Меньше нуля')
# else:
#         print('Больше нуля')
# print('До свидания!')
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# import pprint
# fib1, fib2 = 1, 1
# n = input('Номер элемента ряда Фибоначчи: ')
# n = int(n)
# i = 0
# while i < n-2:
#     print(fib2)
#     next_fib2 = fib1 + fib2
#     next_fib1 = fib2
#     fib1, fib2 = next_fib1, next_fib2
#     i += 1
# print('Значение этого элемента: ', fib2)
# for number in [0, 1, 2, 3, 4]:
#     print(number)
# a_dict = {"one":1, "two":2, "three":3}
# for key in a_dict:
#     print(key)
# a_dict = {3:"three", 2:"two", 1:"one"}
# keys = a_dict.keys()
# # keys = sorted(keys)
# for key in keys:
#     print(key)
# room_prices = [41, 94, 100, 7, 21, 92, 62, 49, 37, 17, ]
# for orange in room_prices:
#     print('Текущая цена:', orange)
# print('До свидания!')
# print('Здравствуй!')
# 
# room_prices = [7, 41, 94, 100, 21, 92, 62, 49, 37, 17, ]
# for price in room_prices:
#     if price == min(room_prices):
#         print('Минимальная цена:', price)
#         if price == 7:
#             print('ещё 1 строка текста')
#             continue
#             print('ещё 2 строка текста')
#     if price == max(room_prices):
#         print('Максимальная цена:', price)
#         continue
#         print('ещё 3 строка текста')
#     print('Текущая цена:', price)
#     # break
# print('До свидания!')
# 
# number = 1 #Number is initially 1 
# while True : #This means the loop will continue infinite time 
#     print (number) #print the number 
#     number+=2 #calculate next odd number # Now give the breaking condition 
#     if number > 10:
#         break #Breaks the loop if number is greater than ten 
#         print (number) #This statement won't be executed
# 
# s1 = "Дата заказа:2018-10-14_аорыроарыов"
# s2= '' # создадим строку для цифр
# s3= '' # создадим строку для букв и символов
# for i in s1:
#     if i.isdigit() == True: # является ли символ цифрой
#         s2 +=i # Добавить символ строку s2
#         print ('Найдена цифра: ', i) 
#     else:
#         s3 +=i # Добавить символ строку s3
#         print ('Буква или символ: ', i) 
#         # pass # пропустить символ
#     print (' s2: ', s2, '\n', 's3: ', s3) 
# 
#   нельзя удалять элементы списка, по которому проходит цикл. решение:
# hotel_names1 = ['aloHotel', 'Appart lounge', 'Sleepower', 'Penthouseus']
# hotel_names2 = ['aloHotel', 'Appart lounge', 'Sleepower', 'Penthouseus']
# print(hotel_names1)
# for name_1 in hotel_names1:
#     print('h1 на позиции: ', name_1)
#     name_2 = name_1
#     hotel_names2.remove(name_2)
#     print(' удалить в h2: ', name_1, '\n', 'hotel_names2: ', hotel_names2)
# print(hotel_names2)
# 
# x, y, z = 1, 2, 3
# (x, y, z) = (1, 2, 3)
# print (x, y, z)
# 
# phone_list = [
# '+7(412)921-53-11',
# '+7 (721) 043-1277',
# '86718915900',
# '+7(012)438-11-95',
# ]
# for phone_number in phone_list:
#     print(phone_number)
#     for i in phone_number:
#         char_is_digit = i.isdigit()
#         print(i, char_is_digit)
# pass
# 
# hotel_prices = {}
# hotel_prices['aloHotel'] = 94
# hotel_prices['Appart lounge'] = 100
# hotel_prices['Sleepower'] = 49
# hotel_prices['Penthouseus'] = 37
# hotel_prices['Hotel star'] = 7
# total_sum = 0
# for hotel_name in hotel_prices:
#     price = hotel_prices[hotel_name]
#     print(hotel_name, price)
#     total_sum += price
# print('Общая стоимость гостиниц =', total_sum)
# print(hotel_prices)
# 
# hotel_prices = {}
# hotel_prices['aloHotel'] = 94
# hotel_prices['Appart lounge'] = 100
# hotel_prices['Sleepower'] = 49
# hotel_prices['Penthouseus'] = 37
# hotel_prices['Hotel star'] = 7
# total_sum = 0
# for hotel_name, price in hotel_prices.items():
#     print(hotel_name, price)
#     total_sum += price
# print('Общая стоимость гостиниц =', total_sum)
# print(hotel_prices)
# 
# def greeting(parameter1):
#     print('Привет,', parameter1, '!')
# hello_list = ['Мир', 'Земля', 'Космос', 'Марк']
# for _ in hello_list:
#     print('Начало цикла')
#     greeting(parameter1=_)
#     print('Конец цикла')
# 
# def make_coffee(size, sugar_dose=3):
#     if sugar_dose > 5: return f'Слишком много сахара! :('
#     else: return f'Заберите ваш кофе объемом {size} мл с {sugar_dose} кусочками сахара'
# size = int(input('Введите объём чашки: '))
# sugar_dose = int(input('Введите количество сахара: '))
# print(make_coffee(size, sugar_dose))
# 
# def trapezoid_s(a,b,h):
#     return h*(a+b)/2
# # param_lst = [2, 3, 4]
# param_dict = {'b': 8, 'h': 4, 'a': 10}
# # S = trapezoid_s(8,4,10)
# # S = trapezoid_s(b=8,h=4,a=10)
# S = trapezoid_s(** param_dict)
# print(S)
# 
# varOne = 1
# varTwo = 2
# print(varOne and varTwo)
# 
# var = 5
# print(type(type(var)))
# 
# var = 'Индексация строк в Python!'
# print(var[3::-1])
# 
# lst = [2, 3, 4]
# num = '1'
# for i in lst:
#     num = num + i
# print(num)
# 
# lst = [-2, -1, 0, 1, 2]
# def func(x):
#     return x < 1
# rst = filter(func, lst)
# print(list(rst))
# 
# import pandas as pd
# import numpy as np
# s = pd.Series(np.random.randn (5), index = ['a', 'b', 'c', 'd', 'e']),
# print(pd.__version __)
# 
import pandas as pd
import numpy as np

# s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])
# print (s)
# print (s['a'])

# import pandas as pd
# import numpy as np
# #print(pd.__version__)
# df = pd.DataFrame(np.random.randn(5,3),
# index = pd.date_range ('1/1/2023', periods = 5),
# columns = ['test', 'test1', 'C'])

# print(df)
# df.describe()

# import pandas as pd
# import numpy as np

# xl = pd.read_excel("data.xlsx", sheet_name = 'Sheet1')
# print(xl.columns)

# import pandas as pd
# import numpy as np
# s = pd.Series([1, 2, 3, 4, 5])
# s = s.replace(1,3)
# print(s)

# df = pd.DataFrame ({'A': [0, 1, 2, 3, 4],
# 'B': [5, 6, 7, 8, 9],
# 'C': ['a', 'b', 'c', 'd', 'e']})
# df = df.replace('a', 5)
# print(df)
# df.to_csv('test.csv')

# import pandas as pd
# import numpy as np

# xl = pd.read_excel("data.xlsx", sheet_name = 'Sheet1')


# kiwi = xl[xl['sku'] == 'Киви']
# kiwi2 = xl[xl['sku'] == 'Киви']

# kiwi2 = kiwi[kiwi['priceoforder'] > 1000]
# print (kiwi2)
# kiwi2.to_excel('task2.xlsx')
# 
# import sqlite3
# import pandas as pd
# connection = sqlite3.connect('Students.db')
# cursor = connection.cursor()
# query = """SELECT * FROM Students;"""
# cursor.execute(query)
# records = cursor.fetchall()
# print(records)
# df = pd.read_sql("SELECT * FROM Students;", connection)
# connection.close()
# print (df)
# df.to_excel('test1.xlsx', index = False)
# ошибки
# import sqlite3
# import pandas as pd
# connection = sqlite3.connect('Students.db')
# cursor = connection.cursor()
# query = """SELECT * FROM Students;"""
# cursor.execute(query)
# records = cursor.fetchall()
# print(records)
# df = pd.read_sql("SELECT * FROM Students;", connection)
# df_newstd = pd.DataFrame({
#     "Student_id":[205,206,207],
#     "Student_name":["Ирина","Ксения","Жанна"]
#     })
# df_newstd.to_sql("Students", con = connection, if_exists = "append", index = False)
# df_newstd.to_excel('task2.xlsx', index = False)
# 
# import sqlite3
# import pandas as pd
# connection = sqlite3.connect('Students.db')
# df = pd.read_sql("SELECT * FROM Students;", connection)
# df.to_sql("Students", con = connection, if_exists = "append", index = False)
# df = pd.DataFrame ({
#   "Student_id":[208,209,210],
#   "Student_name": ["Ирина","Ксения","Жанна"],
#   "School_Id": [1,2,3]
#   })
# df.to_excel('Taskuch2.xlsx', index = False)
# 
# import numpy as np
# x = np.matrix('9 8 7; 6 5 4; 3 2 1')
# print(x[0, 2])
# x.tolist()
# import numpy as np
# x = np.diag([16, 5, 8, 10, 9, 1])
# print(x)
# np.savetxt('task4.csv', x, delimiter=',', fmt ='%s')
# 
# import numpy as np
# x = np.arange(1, 17).reshape((4, 4))
# print(x)
# 

# import numpy as np
# x = np.array([1, 2, 3, 4])
# print("Входящий массив:")
# print(x)
# print("Проверка на наличие элемента со значением 0")
# print(np.all(x))
# x = np.array([0, 1, 2, 3])
# print("Входящий массив:")
# print(x)
# print("Проверка на наличие элемента со значением 0:")
# print(np.all(x))
# 
# import numpy as np
# x = np.arange(0,49).reshape((7,7))
# print (np. sum (x, axis= 0))
# print (np. sum (x, axis= 1))
# print (np. sum (x))
# np.savetxt('task6.csv', x, delimiter=',', fmt ='%s')
# 
# import numpy as np
# x = np.random.randint(low = 10, high = 40, size =6)
# xmin, xmax = x.min(), x.max()
# print(x)
# print(xmin, xmax)
# 
import numpy as np
x = np.random.randint((5, 5))
xmin, xmax = x.min(), x.max()
print(x)
print(xmin, xmax)