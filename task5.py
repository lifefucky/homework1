"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них."""

array = []


while True:
    user_input = input("Please insert new element, press a letter or symbol to quit\n")
    if not user_input.isdigit():
        break
    else:
        user_input = int(user_input)
    if len(array)==0:
        array.append(user_input)
        continue
    for idx in range(len(array)):
        is_bigger = 0
        user_index = idx
        if user_input>array[idx]:
            is_bigger=1
            break
    if is_bigger:
        array.insert(user_index,user_input)
    else:
        array.append(user_input)
    print(array)