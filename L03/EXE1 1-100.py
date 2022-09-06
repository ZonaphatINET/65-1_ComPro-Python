#1-100 กำหนดบันทัด (กำหนด rows)
print("1 - 100")
columns = int(input('Enter your : '))
for i in range (1,101):
    print(i,end='\t')
    for j in range(0,101,columns):
        if i == j:
            print()  