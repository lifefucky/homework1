"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
with open('sample_text3.txt', 'r', encoding='UTF-8') as sample_text:
    poor_stuff = [i.split(' ')[0] for i in sample_text.readlines() if float(i.replace('\n','').split(' ')[1])<20000]
    sample_text.seek(0)
    incomes = [float(a.replace('\n','').split(' ')[1]) for a in sample_text.readlines()]

    avg_income = sum(incomes)/len(incomes)
    print(poor_stuff, avg_income)