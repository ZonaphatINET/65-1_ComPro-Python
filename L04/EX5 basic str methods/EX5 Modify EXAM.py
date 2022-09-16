inputsmg = input("In put string you want to swao words: ")
print(inputsmg.split())
separatewrods = inputsmg.split()

print("separate wrods")
for i in separatewrods:
    print(i)

print("Modify each words")
print(len(separatewrods))
for j in range(len(separatewrods)):
    separatewrods[j] = 'G' + separatewrods[j]
    print(separatewrods[j])

print(separatewrods)
print(" ".join(separatewrods),)