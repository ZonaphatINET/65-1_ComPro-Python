rows = int(input('Enter your rows: '))
columns = int(input('Enter your columns: '))
num = 0
while num < columns :
    for i in range(1,11):
        print()
        for j in range(rows):
            print(i,end="")
            num += 1