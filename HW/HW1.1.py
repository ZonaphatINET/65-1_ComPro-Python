agean = 'y'
while agean == 'y' :
    neme = str(input("Enter your name = "))
    item = str(input("Enter item ID: "))
    pri = int(input('Enter your price: ฿'))
    num = int(input("Enter amount item: "))
    if item.startswith('P1') :
        item_pay = pri * num
        pay = item_pay - ((item_pay / 100) * 3)
        print("Price: ",pay)
    elif item.startswith('P2') :
        if num <= 3 :
            item_pay = pri * num
            pay = item_pay - ((item_pay / 100) * 3)
            print("Price: ",pay)
        else:
            item_pay = pri * num
            pay = item_pay - ((item_pay / 100) * 5)
            print("Price: ",pay,'฿')
    elif item.startswith('P3') :
        item_pay = pri * num
        pay = item_pay
        print("Price: ",pay,'฿')
    else:
        print("Oh!!! Sory Not found ID ?")
    agean = input('Want to repeat? ( y or n ) : ')