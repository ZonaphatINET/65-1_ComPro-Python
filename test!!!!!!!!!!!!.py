#1-100 กำหนดบันทัด (กำหนด rows)
print("1 - 100")
B = int(input('Enter your rows: '))
B -= 1
if B == 0:
    B += 1
elif B == 1:
    B += 1
A = 100 // B 
for i in range (1,101):
    print(i,end='')
    for j in range(0,101,A):
        k = j % A
        if i == j:
            print() 

