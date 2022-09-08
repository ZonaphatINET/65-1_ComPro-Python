def main():
    emp_file = open("employees.txt",'r')
    name = input('Enter name your want to find : ').split()

    for mem in emp_file :
        amo = str(mem)
        if amo.find(name):
            print(amo.strip('\n'))
        else:
            print('...')
    
    emp_file.close()

main() 