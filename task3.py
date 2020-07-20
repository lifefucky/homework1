"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

numb = input("insert number\n")

while True:
    if numb.isdigit():
        numb = int(numb)
        break
    else:
        print('Incorrect input. Try again')


seasons = {
    'зима': (12,1,2),
    'весна': (3,4,5),
    'лето': (6,7,8),
    'осень': (9,10,11)
}

for key, value in seasons.items():
    if numb in value:
        print(key)
        break
