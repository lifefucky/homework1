"""Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя."""

product_template  = {
    'Names':('ProductName',str),
    'Prices':('Price', float),
    'Quantity':('Quantity', int),
    'Definition':('Definition value', str)
}

user_products = []
auto_inc = 1

while True:
    next_product=0
    product = {}
    for key, value in product_template.items():
        while True:
            user_input = input(f'Please insert {value[0]}')
            user_input = value[1](user_input)
            product[key] = user_input
            break
    user_products.append((auto_inc, product))
    auto_inc+=1
    
    while True:
        user_continue = input("Continue insert? Y/N")
        if user_continue.lower()=='y':
            next_product = 1
            break
        elif user_continue.lower()=='n':
            break
        else:
            print('Incorrect input!')
    if next_product==0:
        break

product_output = {}

for i in product_template:
    array =[]
    for j in user_products:
        array.append(j[1][i])
    product_output[i] = array

print(product_output)

