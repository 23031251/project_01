# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

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

# Решение А
import random
import datetime
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
selection = random.sample(my_favorite_songs, k=3)
# print(selection)
print("Задание A. Три песни к прослушиванию: ", selection[0][0], ", ", selection[1][0], ", ", selection[2][0])
timeList = [selection[0][1], selection[1][1], selection[2][1]]
# print(timeList)
duration_m_s = datetime.timedelta()
for p in timeList:
    p = str(p)
    (m, s) = p.split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    duration_m_s += d
# print(str(duration_m_s))
hms = str(duration_m_s)
# print("hms: ", hms)
hh, mm, ss = hms.split(':')
hhh = int(hh)
mmm = int(mm)
duration_m = hhh * 60 + mmm
# print("duration_m: ", duration_m)
print (f"Три песни звучат", duration_m, "минут" )

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Решение B
import random
import datetime
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
my_favorite_songs2 = list(my_favorite_songs_dict)    
# print(my_favorite_songs)
selection = random.sample(my_favorite_songs2, k=3)
print("Задание B. Три песни к прослушиванию: ", selection)
duration_m_s = datetime.timedelta()
for g in selection:
    p = str(my_favorite_songs_dict[g])
    (m, s) = p.split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    duration_m_s += d
    # print(d)
# print(duration_m_s)
hms = str(duration_m_s)
# print("hms: ", hms)
hh, mm, ss = hms.split(':')
hhh = int(hh)
mmm = int(mm)
duration_m = hhh * 60 + mmm
# print("duration_m: ", duration_m)
print (f"Три песни звучат", duration_m, "минут" )


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

#  Решение C, D
import random
import datetime
my_favorite_songs3 = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
import datetime
my_favorite_songs4_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
selection2 = random.sample(my_favorite_songs3, k=4)
# print(selection)
print("Задание C+A. Четыре песни к прослушиванию: ", selection2[0][0], ", ", selection2[1][0], ", ", selection2[2][0], ", ", selection2[3][0])
my_favorite_songs4 = list(my_favorite_songs4_dict)    
# print(my_favorite_songs)
timeList2 = [selection2[0][1], selection2[1][1], selection2[2][1]]
# print(timeList)
duration_m_s = datetime.timedelta()
for p in timeList2:
    p = str(p)
    (m, s) = p.split('.')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    duration_m_s += d
print("Задание D+A. Полное время звучания: ", str(duration_m_s))
selection = random.sample(my_favorite_songs4, k=4)
print("Задание C+B. Четыре песни к прослушиванию: ", selection)

