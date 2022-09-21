moreHeroes = int(input('Enter number your heroes : '))
heroes = [0] * moreHeroes
for index in range(moreHeroes):
    print('Enter name heroes ',index +1 ,' : ',sep='',end='')
    heroes[index] = str(input())

def inputHeroes():
    print(heroes)

def insert():
    Hero = input('Enter name to add : ')
    index = int(input('Enter location name : '))
    heroes.insert(index,Hero)
    inputHeroes()

def remove():
    Hero = input('Enter name to remove : ')
    heroes.remove(Hero)
    inputHeroes()

def Dissort():
    heroes.sort()
    inputHeroes()

def reverse():
    heroes.reverse()
    print(heroes)

def main():
    inputHeroes()
    insert()
    remove()
    Dissort()
    reverse()

main()
