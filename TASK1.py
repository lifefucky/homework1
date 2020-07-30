"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open('sample_text.txt', 'w', encoding='UTF-8') as sample_text:
    while True:
        user_input = input("Please enter string:\n")
        if not len(user_input):
            break
        sample_text.write(f'{user_input}\n')
