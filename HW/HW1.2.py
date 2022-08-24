one_inch = 65
two_inch = 80
polaroid = 70
agean = 'y'
while agean == 'y' : 
    name = str(input("Enter name: "))
    print('type Photo')
    print("1. One inch ")
    print("2. Two inch ")
    print("3. Polaroid ")
    menu = int(input("Enter type: "))
    num = int(input("Enter amount: "))
    print('______________________')
    print('Your name is ',name)
    if menu == 1 :
        if num <= 3 :
            item_pay = num * one_inch
            print('Your type is One inch')
            print('Your amount is ',num)
            print('You have to pay : ',item_pay,'฿')
        else :
            item_pay = num * one_inch
            pay = item_pay - ((item_pay / 100) * 5)
            print('Your type is One inch')
            print('Your amount is ',num)
            print('You have to pay : ',pay,'฿')
    elif menu == 2 :
        if num <= 3 :
            item_pay = num * two_inch
            print('Your type is Two inch')
            print('Your amount is ',num)
            print('You have to pay : ',item_pay,'฿')
        else :
            item_pay = num * two_inch
            pay = item_pay - ((item_pay / 100) * 5)
            print('Your type is Two inch')
            print('Your amount is ',num)
            print('You have to pay : ',pay,'฿')
    elif menu == 3 :
        item_pay = num * polaroid
        print('Your type is Polaroid')
        print('Your amount is ',num)
        print('You have to pay : ',item_pay,'฿')
    else :
        print('Not found menu')
    print('______________________')
    agean = input('Want to repeat? ( y or n ) : ')
    

