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
# import pandas as pd
# import numpy as np

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
# import numpy as np
# x = np.random.randint((5, 5))
# xmin, xmax = x.min(), x.max()
# print(x)
# print(xmin, xmax)
# 
# import random
# print(random.randint(0, 5))
# import pandas 
# import matplotlib
# import seaborn
# import os
# reviews = pandas.read_csv(f'{os.getcwd()}\winemag-data_first150k.csv.gz', compression='gzip')
# reviews.head()
# 
# import random
# # --- from datetime import timedelta
# import datetime

# my_favorite_songs = [
#     ['Waste a Moment', 3.03],
#     ['New Salvation', 4.02],
#     ['Staying\' Alive', 3.40],
#     ['Out of Touch', 3.03],
#     ['A Sorta Fairytale', 5.28],
#     ['Easy', 4.15],
#     ['Beautiful Day', 4.04],
#     ['Nowhere to Run', 2.58],
#     ['In This World', 4.02],
# ]

# selection = random.sample(my_favorite_songs, k=3)
# print(selection)
# print("Три песни: ", selection[0][0], ", ", selection[1][0], ", ", selection[2][0])
# --- duration = selection[0][1] + selection[1][1] + selection[2][1]
# ??? print (f"Три песни звучат ", duration, " минут" )
# --- d = timedelta(my_favorite_songs[2][1] + my_favorite_songs[4][1])
# --- print(f"Проверка корректности сложения 3.40+5.28=", d)



# timeList = [selection[0][1], selection[1][1], selection[2][1]]
# print(timeList)
# duration_m_s = datetime.timedelta()
# for p in timeList:
#     p = str(p)
#     (m, s) = p.split('.')
#     d = datetime.timedelta(minutes=int(m), seconds=int(s))
#     # d_m = datetime.timedelta(minutes=int(m))
#     duration_m_s += d
    # duration_m += d_m
    # dd = 
# print(str(duration_m_s))
# hms = str(duration_m_s)
# print("hms: ", hms)
# hh, mm, ss = hms.split(':')
# hhh = int(hh)
# mmm = int(mm)
# print("hhh+1: ", hhh+1)
# print(hh, mm, ss * 4)
# duration_m = hhh * 60 + mmm
# print("duration_m: ", duration_m)
# --- duration_m = datetime.timedelta()

# --- d_s = datetime.timedelta(minutes=int(m), seconds=int(s))
# hours, minutes, seconds = timedelta_to_hms(duration_m_s)
# print(f'{hours} hours, {minutes} minutes')
# print (f"Три песни звучат ", duration_m, " минут" )
# 
# vocabulary = { 'а' : ('ананас', 'апельсин', 'арбуз'),
# 'б' : ('баклажан','батат', 'брюква') }
# book = vocabulary
# book['в'] = ('виноград')
# print(vocabulary,'\n',book)
# # capitals == vocabulary
# book.get('батат', 'Отсутствует')
# 

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
# import random
# import datetime
# my_favorite_songs_dict = {
#     'Waste a Moment': 3.03,
#     'New Salvation': 4.02,
#     'Staying\' Alive': 3.40,
#     'Out of Touch': 3.03,
#     'A Sorta Fairytale': 5.28,
#     'Easy': 4.15,
#     'Beautiful Day': 4.04,
#     'Nowhere to Run': 2.58,
#     'In This World': 4.02,
# }
# d = my_favorite_songs_dict
# # print(my_favorite_songs_dict)
# # dicttolist = list(my_favorite_songs_dict)
# # selection = random.choice(list(my_favorite_songs_dict))
# # print(dicttolist)
# # # selection = my_favorite_songs_dict['New Salvation']
# # # selection = random.sample(my_favorite_songs_dict, k=3)
# # print(selection)
# # print("Три песни: ", selection[0][0], ", ", selection[1][0], ", ", selection[2][0])
# # timeList = [selection[0][1], selection[1][1], selection[2][1]]
# # print(timeList)
# # duration_m_s = datetime.timedelta()
# # for p in timeList:
# #     p = str(p)
# #     (m, s) = p.split('.')
# #     d = datetime.timedelta(minutes=int(m), seconds=int(s))
# #     # d_m = datetime.timedelta(minutes=int(m))
# #     duration_m_s += d
# #     # duration_m += d_m
# #     # dd = 
# # print(str(duration_m_s))
# # hms = str(duration_m_s)
# # # print("hms: ", hms)
# # hh, mm, ss = hms.split(':')
# # hhh = int(hh)
# # mmm = int(mm)
# # # print("hhh+1: ", hhh+1)
# # # print(hh, mm, ss * 4)
# # duration_m = hhh * 60 + mmm
# # # print("duration_m: ", duration_m)
# # # --- duration_m = datetime.timedelta()

# # # --- d_s = datetime.timedelta(minutes=int(m), seconds=int(s))
# # # hours, minutes, seconds = timedelta_to_hms(duration_m_s)
# # # print(f'{hours} hours, {minutes} minutes')
# # print (f"Три песни звучат ", duration_m, " минут" )
# # print(my_favorite_songs_dict.get()) 
# # print(my_favorite_songs_dict.keys())
# # print(my_favorite_songs_dict.values())
# # print(my_favorite_songs_dict.items())
# my_favorite_songs = list(my_favorite_songs_dict)    #.keys())
# # ww = w.split(',', -1)
# print(my_favorite_songs)
# # u = random.choices(my_favorite_songs_dict, weights=None, *, cum_weights=None, k=3)
# # random.choice(d.keys())
# # print(u)
# # print(type(my_favorite_songs_dict))
# # ww = w(10;-1)

# selection = random.sample(my_favorite_songs, k=3)
# print("Три песни к прослушиванию: ", selection)
# duration_m_s = datetime.timedelta()
# for g in selection:
#     p = str(my_favorite_songs_dict[g])
#     (m, s) = p.split('.')
#     d = datetime.timedelta(minutes=int(m), seconds=int(s))
#     duration_m_s += d
#     # print(d)
# # print(duration_m_s)
# # --- print(str(duration_m_s))
# hms = str(duration_m_s)
# # print("hms: ", hms)
# hh, mm, ss = hms.split(':')
# hhh = int(hh)
# mmm = int(mm)
# duration_m = hhh * 60 + mmm
# # print("duration_m: ", duration_m)
# print (f"Три песни звучат", duration_m, "минут" )
# 
# dict = {
# 1: 'январь. 31 день',
# 2: 'февраль. 28 дней',
# 3: 'март. 31 день',
# 4: 'апрель. 30 дней',
# 5: 'май. 31 день',
# 6: 'июнь. 30 дней',
# 7: 'июль. 31 день',
# 8: 'август. 31 день',
# 9: 'сентябрь. 30 дней',
# 10: 'октябрь. 31 день',
# 11: 'ноябрь. 30 дней',
# 12: 'декабрь. 31 день', 
# }

# n = input("Введите номер месяца: ")
# # print(type(n))
# m = int(n)
# # print(m)
# if 1 <= m <= 12:
#     print("Вы ввели", dict[m])
# else: 
#     print("Такого месяца нет!")
# 
# Задача 1.4.

# Есть словарь кодов товаров titles

# titles = {
#     'Кроссовки тип 3 (Adidas)': '100000110',
#     'Мячик тип 2 (Adidas)': '100000146',
#     'Кепка тип 1 (Adidas)': '100000149',
#     'Ремень тип 2 (Nike)': '100000194',
#     'Футболка тип 1 (Adidas)': '100000224',
#     'Шапка тип 5 (Puma)': '100000280',
# }

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

# store = {
#     '100000110': [{'quantity': 31, 'price': 1637}],
#     '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
#     '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
#     '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
#     '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
#     '100000280': [{'quantity': 26, 'price': 175}, ]
# }

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

# d = {}
# for x in store:
#      q, p = x['quantity'], x['price']
#      d[c] = store.get(q, 0) * store.get(p, 0)
# print(d)


# test = {'quantity': 31, 'price': 1637}
# print(test.values())

# +++ print(store['100000149'][1])
# +++ print(store['100000149'])
# ,,, print(type(store['100000149'])) #<class 'list'>
# print(store['100000149'][1].get('quantity'), store['100000149'][1].get('price'))
# print(store['100000149'][1].get())  # TypeError: get expected at least 1 argument, got 0
# --- print(store['100000149'][1].values('quantity'))  # TypeError: dict.values() takes no arguments (1 given)
# print(store['100000149'].values())  #AttributeError: 'list' object has no attribute 'values'
# s = store['100000224'] #[1]
# ,,, print(type(s))  #<class 'dict'>
# print(s)    #{'quantity': 32, 'price': 291}
# +++ s2 = store['100000149']
# +++ print(s2[1])    #{'quantity': 32, 'price': 291}
# import collections
# d = collections.defaultdict(int)
# cc = 0
# # print(len(titles))
# for name, code in titles.items():       #               обработка первого источника
#     # --- name, code = titles.items()
#     # print('name, code=', name, code)
#     s = store[code] 
#     c = 0
#     r = 0
#     qq = 0
#     for k in range(len(s)):         #                   проход по списку линии второго источника
        
        
        # print('c=', c)
    # for i in list1:
    # d[k['quantity']] += k['price']
    # o = s[k]
    # print(o)
    # q, p = o.get('quantity'), o.get('price')
    # q, p = s[k].get('quantity'), s[k].get('price')
    #                                               внутри линейного словаря
        # q = s[k].get('quantity')
        # # print('q=', q)
        # r = s[k].get('quantity') * s[k].get('price')
        # print('r =', r)

        # c += r         # начало набора стоимости линии

        # qq += q              # начало набора количества линии
        # print('q=', q)
        # print('qq=', qq)
        # print('конец итерации внутри линейного словаря')
    # print('q, p =', q, p) #+++
#     # print('r =', r)
#     print('"', name, ' - ', qq, ', стоимость ', c, ' руб"')
#     # print('конец итерациивнутри линейного линии')
#     cc += c
# print('На складе товаров на', cc, 'рублей')
# 
# # Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# # функции max и min использовать нельзя!
# import random
# base0 = list(range(-20, 20, 2))
# print(base0)
# # list = [20, 30, 40, 50 ,60, 70, 80, 90]
# a = random.choices(base0, k=10)
 
# print("Произвольный список: ", a)

# a = [4, 6, 2, 1, 9, 63, -134, 566]
# arr = [14, 16, 12, 11, 19, 163, -1134, 1566]
# +++ arr.sort() 
# +++ print(arr)
# def minimum(arr):
#     arr.sort()  
#     m = arr[0]
#     return m
#     # pass
# def maximum(arr):
#     arr.sort()  
#     b = arr[-1]
#     return b
    # pass
# minimum(a)
# print(a[0])
# b = minimum(a)
# maximum(a)
# print('minimum(a)=', minimum(a))
# print('maximum(a)=', maximum(a))
# a.sort()
# print('min=', b)
# print('min=', a)


# spisok = [2, 3, 5, 7, 11, 13] # нельзя применять по условиям задачи
# print(min(spisok))

# spisok = [2, 13, 5, 7, 11, 13]
# < spisok.sort()
# < print(spisok)
# > [2, 5, 7, 11, 13, 13]
# salary = input('Введите зарплату ')
# expenses = input('Введите расходы ')

# x = int(salary)
# y = int(expenses)
# n = 12

# if y>=x:
#     print('Неверные данные')
# else:
#     p=[]
#     i=1
#     for i in range(n):
#         i += i
#         x = 1.05 * x
#         p.append(x)
#     sum(p)

# print('Сотрудник накопит ', '%.2f' % (sum(p) - n * y), ' руб')
# 
# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.
# opis_mes = {
#     1: 'месяц 1 (январь)',
#     2: 'месяц 2 (февраль)',
#     3: 'месяц 3 (март)',
#     4: 'месяц 4 (апрель)',
#     5: 'месяц 5 (май)',
#     6: 'месяц 6 (июнь)',
#     7: 'месяц 7 (июль)',
#     8: 'месяц 8 (август)',
#     9: 'месяц 9 (сентябрь)',
#     10: 'месяц 10 (октябрь)',
#     11: 'месяц 11 (ноябрь)',
#     12: 'месяц 12 (декабрь)'    
# }
# opis_kvart = {
#     1: 'является частью первого квартала',
#     2: 'является частью второго квартала',
#     3: 'является частью третьего квартала',
#     4: 'является частью четвертого квартала'
# }

# # k = 1
# def quarter_of(month):
#     k = 1
#     while k in range(1, 5):
#         # k = p
#         if month - (3 * k) <= 0:
#             print('chekpoint', k)
#             print('K=', k)
#             return k
#             # break
#         else:
#             k += 1
#             print('chekpoint', k)
#     # return k
# x = int(input('Введите номер месяца:'))
# try:
#     1 <= x <= 12
# except KeyError:
#     print('Введите номер месяца от 1 до 12')
# quarter_of(x)
# print(opis_mes[x], opis_kvart[quarter_of(x)])
# print(opis_mes[1])

# исключения по вводу не доделал
# x = int(input('Введите номер месяца:'))
# try:
#     1 <= x <= 12
#     print('Норма')
# # except:
#     # print('Нужен номер месяца')
# except ValueError:
#     print('Это не число. Выходим.')
# except Exception:
#     print('Это что ещё такое?')
    # 
# Задача 2.3.
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
a = int(input(' Введи делимое:'))
b = int(input(' Введи делитель:'))
try:
    a = int
    b = int
    y = a / b
    print('a=', a)
    print('b=', b)
    print('y=', y)
    x in (range(0, 9))
except ValueError:
    print('Что-то не то ввели')

# except ZeroDivisionError:
#     print('Ошибка! Деление на 0')
def switch_it_up(number):
    number = int(input('Введите цифру:'))
    return number
# switch_it_up(x)
# quarter_of(x)
print(opis_cifr.get(switch_it_up(x)))