"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def num_division(a, b):
    try:
        c = float(a)/float(b)
        return c
    except ZeroDivisionError as e:
        print('Division by zero')
        pass
    except ValueError as v:
        print("Incorrect input")
        pass




while True:
    user_continue = 0
    a, b = input("Please insert numbers:\n").split(' ')
    if not num_division(a, b) is None:
        print(f'{num_division(a, b):.2f}')
    ans = input("Continue?y/n\n").lower()
    if ans in ('y','n'):
        if ans == 'n':
            break











