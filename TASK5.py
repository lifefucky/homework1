"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random


random_numbers = [random.randint(1, 100) for _ in range(random.randint(2, 100))]


with open('sample_text5.txt', 'w', encoding='UTF-8') as sample_text:
    numbers_str = ' '.join(map(str, random_numbers))
    sample_text.write(numbers_str)

with open('sample_text5.txt', 'r', encoding='UTF-8') as sample_text:
    numbers = map(int, sample_text.read().split(' '))


print(sum(random_numbers)==sum(numbers))