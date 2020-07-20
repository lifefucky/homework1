"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

user_input = input("Insert list of numbers delimited by comma\n")
array = user_input.split(',')

idx = 0
while idx<len(array)-1:
    array[idx], array[idx+1] = array[idx+1], array[idx]
    idx+=2
print(array)


