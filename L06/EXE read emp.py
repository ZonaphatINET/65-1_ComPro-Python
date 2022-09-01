from itertools import count
from os import name


def main():
    sales_file = open('employees.txt','r')
    name = 1
    id = 2
    dept = 3
    num = 3
    count = 1
    for line in sales_file:
        amount = str(line)
        if name == count:
            print('Name:',amount.rstrip('\n'))
            name += num
            count += 1
        elif id == count:
            print('ID:',amount.rstrip('\n'))
            id += num 
            count += 1
        elif dept == count:
            print('Dept:',amount.rstrip('\n'))
            dept += num 
            count += 1
        else:
            print()

    sales_file.close

main()