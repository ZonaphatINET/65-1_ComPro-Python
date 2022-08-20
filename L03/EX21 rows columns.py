rows = int(input('Enter your rows: '))
columns = int(input('Enter your columns: '))
num = 0
while num < columns :
    for j in range(rows):
        print("* ",end="")
    num += 1
    print()