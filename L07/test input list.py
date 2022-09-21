moreHeroes = int(input('Enter number your heroes : '))

def inputHeroes():
    heroes = [0] * moreHeroes

    for index in range(moreHeroes):
        print('Enter name heroes ',index +1 ,' : ',sep='',end='')
        heroes[index] = str(input())

    print(heroes)

inputHeroes()


