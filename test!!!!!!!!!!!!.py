lijst = list(range(1, 11))
i = 0
columns = int(input('Enter your columns: '))
while i < 100:
    print(lijst[i],)
    i = i+1
    if i % columns == 0:
        print("")