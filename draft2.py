# Задача 2.4.

# Пункт A. Решение
source_string = str
def remove_exclamation_marks(s):
    s = input('Введите строку с восклицательным знаком или нажмите ввод: ') or '!!!test!!!'
    if s == '!!!test!!!': 
        print('Тестовый исходник: !!!test!!!')
    s = s.replace('!', '')
    return s
print('Очищенная строка:', remove_exclamation_marks(source_string))

# Пункт B. Решение
source_string = str
def remove_last_em(s):
    s = input('Введите строку с восклицательным знаком или нажмите ввод: ') or '!!!test!!!'
    if s == '!!!test!!!': 
        print('Тестовый исходник: !!!test!!!')
    s = s[:-1]
    return s
print('Очищенная строка:', remove_last_em(source_string))

# Пункт C. Решение
source_string = str
def remove_word_with_one_em(s):
    s = input('Введите строку, содержащую слова как с восклицательным знаком так и без. Если лень, нажмите ввод: ') or 'раз! два!! три!!! !четыре!!! раз! два!!'
    if s == 'раз! два!! три!!! !четыре!!! раз! два!!': 
        print('Тестовый исходник: Hi! !Hi! Hi')   
        # s = s[:-1]
    spisok = s.split()
    print('исходный список: ', spisok)
    n = 0
    for p in spisok:
        a = len(p)
        # print('начальная длина строчного элемента', n, ': ', a)
        p = p.replace('!', '')
        b = len(p)
        # print('итоговая длина строчного элемента', n, ': ', b)
        if a == b + 1:
            spisok.pop(n)
        n += 1
    # print('spisok=', spisok)
    s = ' '.join(spisok)
    return s
print('Очищенная строка:', remove_word_with_one_em(source_string))