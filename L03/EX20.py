next = 'y'
while next == 'y':
    wholesale_cost = float(input("Enter the item's wholesale cost : "))
    retail_price = wholesale_cost * 2.5
    print("Retail price: $%.2f" %retail_price)
    next = str(input("Do you have another item? (Enter y for yes) : "))