"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу."""
exit_sum = 0
def user_sum(user_numbers):
    user_continue = 1
    global exit_sum
    for itm in user_numbers:
        try:
            exit_sum+=float(itm)
        except ValueError as v:
            if itm=='q':
                user_continue=0
                break
            else:
                continue
    return user_continue


while True:
    user_inputs = input("Введите числа, разделенные пробелом (если список закончился, введите q):\n").split(' ')
    to_continue = user_sum(user_inputs)
    print(exit_sum)
    if not to_continue:
        break
