from sys import argv

_, hours,pay,bonus = argv

try:
    print(int(hours)*float(pay)+float(bonus))
except ValueError as v:
    print('Unexcepted values inserted')

