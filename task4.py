"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове"""

user_words = input("Please insert words delimited by space\n")
user_array =user_words.split(' ')

for ind, el in enumerate(user_array):
    print(f'{ind} : {el[:10]}')