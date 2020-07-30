"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open('sample_text4.txt', 'r', encoding='UTF-8') as sample_text:
    list_ = [i.replace(i.split(' ')[0], my_dict.get(i.split(' ')[0])) for i in sample_text.readlines()]

with open('alter_sample_text4.txt', 'w', encoding='UTF-8') as sample_text2:
    sample_text2.writelines(list_)

