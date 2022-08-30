def main():
    sales_file = open('employees.txt','r')

    for line in sales_file:
        amount = str(line)
        print(format(amount))

    sales_file.close

main()