#1-100 กำหนดบันทัด (กำหนด rows)
print("1 - 100")
B = int(input('Enter your rows: '))
if 100 % B == 0 :
    B += 0
else:
    B += 1
A = 100 // B 
for i in range (1,101):
    print(i,end=' ')
    for j in range(0,101,A):
        k = j % A
        if i == j:
            print() 

''' Have Errer '''

