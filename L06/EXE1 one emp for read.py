def main():
    emp_file = open("employees.txt",'r')
    name = input('Enter name your want to find : ')

    for mem in emp_file:
        amount = str(mem)
        #print(mem.strip('\n'))
        see = mem.find(name)
        if see >= 0 :
            print('Ok')
        if see == -1:
            print('No')
    emp_file.close()

main() 