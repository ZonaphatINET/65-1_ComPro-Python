records={'6506022420011':['Naphat Thaingtham','Naphat@gmail.com','094970912']}

def displayRecords():
    print(records)

def add():
    number = str(input('Enter ID: '))
    records[number]= [str(input('Enter name: ')),str(input('Enter mail: ')),
                    str(input('Enter phon number: '))]

def Read():
    read = records[str(input('Enter ID: '))]
    print(read)

def Delete():
    del records[str(input('Enter ID: '))]
'''
def Modifile():
    number = str(input('Enter ID: '))
    records[number]= [str(input('Enter name: ')),str(input('Enter mail: ')),
                    str(input('Enter phon number: '))]
'''
def main():
    go = 'y'
    while go == 'y':
        print('Menu')
        print("1.Display Records")
        print("2.Add")
        print("3.Read Records")
        print("4.Modifile")
        print("5.Delete")
        print("6.Exit")
        sw = int(input('Enter number menu: '))
        if sw == 1:
            print(displayRecords())
        elif sw == 2:
            print(add())
        elif sw == 3:
            print(Read())
        elif sw == 4:
            print(add())
        elif sw == 5:
            print(Delete())
        elif sw == 6:
            print('Bye bye :)')
            break
            
main()

