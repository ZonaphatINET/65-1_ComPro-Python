neme = str(input("Enter your name = "))
print('ID\tProduct')
print("G1\tCola\t15 ฿")
print("G2\tLeo\t80 ฿")
print("G3\tMama\t6 ฿")
item = str(input("Enter item ID: "))

if item == 'J011' :
    m1 = int(input('Enter your price: ฿'))
    num = int(input("Enter amount item: "))
    item_pay = m1 * num
    pay = item_pay - ((item_pay / 100) * 3)
    print("ํYou have to pay: ",pay,' ฿')
elif item == 'J023' :
    m2 = int(input('Enter your price: ฿'))
    num = int(input("Enter amount item: "))
    if num <= 3 :
        item_pay = m2 * num
        pay = item_pay - ((item_pay / 100) * 3)
        print("Price: ",pay)
    else:
        item_pay = m2 * num
        pay = item_pay - ((item_pay / 100) * 5)
        print("Price: ",pay,' ฿')
elif item == 'RE224' :
    m3 = int(input('Enter your price: ฿'))
    num = int(input("Enter amount item: "))
    item_pay = m3 * num
    print("Price: ",item_pay,' ฿')
else:
    print("Not found ID ?")