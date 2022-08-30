def main():
    sales_file = open('employees.txt','r')
    i = 1
    j = 2
    k = 3
    l = 3
    m = 1
    for line in sales_file:
        amount = str(line)
        if i == m:
            print('Name: ',amount.rstrip('\n'))
            i += l
            m += 1
        elif j == m:
            print('ID: ',amount.rstrip('\n'))
            j += l 
            m += 1
        elif k == m:
            print('Dept: ',amount.rstrip('\n'))
            k += l 
            m += 1
        else:
            print()

    sales_file.close

main()