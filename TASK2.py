"""Cоздать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('sample_text2.txt', 'r', encoding='UTF-8') as sample_text:

    for idx, itm in enumerate(sample_text.readlines(),1):
        string_lst = sum([1 for i in itm.replace('\n','').split(' ') if len(i)>0])
        print(f'{idx} строка: {string_lst} слов')
