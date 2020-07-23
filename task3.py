"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов."""

def my_func(*d):
    try:
        d = [float(i) for i in d]
    except ValueError as v:
        d = [float(i) for i in d if i.isdigit()]
    d.sort()
    if len(d)>1:
        ans = d[-2]+d[-1]
    else:
        ans = d[0] if len(d)>0 else print("No numbers in list")
    return ans

a,b,c = input("Введите три числа, разделенные пробелом:\n").split(' ')

if not my_func(a,b,c) is None:
    print(my_func(a,b,c))

