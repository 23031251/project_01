# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     pass


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
#     pass


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

# Пункт C. Решение
source_string = str
def remove_word_with_one_em(s):
    s = input('Введите строку, содержащую слова как с восклицательным знаком так и без. Если лень, нажмите ввод: ') or 'раз! два!! три!!! !четыре!!! раз! два!!'
    if s == 'раз! два!! три!!! !четыре!!! раз! два!!': 
        print('Тестовый исходник: раз! два!! три!!! !четыре!!! раз! два!!')
    spisok = s.split()
    # print('исходный список: ', spisok)
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