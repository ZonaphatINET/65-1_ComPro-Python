#1-100 กำหนดบันทัด
print("1 - 100")
columns = int(input('Enter your columns: '))
for i in range (1,101):
    print(i,end=' ')
    for j in range(0,101,columns):
        if i == j:
            print()  