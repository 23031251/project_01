spisok = [2, 13, 5, 7, 11, 13]
spisok4 = ['a', 'b', 'v', 'g', 'd']
stroka = '2, 3, 5, 7, 11, 13'
matrica = [ [4,5] , [7,9] ]
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
spisok2 = spisok
spisok3 = spisok * 3
stroka *= 2
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
import copy
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
i = 0
while i < 5:
    print(i)
    i += 1
