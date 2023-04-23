# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     pass

# Пункт A. Решение
source_string = str
def remove_exclamation_marks(s):
    s = input('Введите строку с восклицательным знаком или нажмите ввод: ') or '!!!test!!!'
    if s == '!!!test!!!': 
        print('Тестовый исходник: !!!test!!!')
    s = s.replace('!', '')
    return s
print('Очищенная строка:', remove_exclamation_marks(source_string))

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

# def remove_word_with_one_em(s):
#     pass