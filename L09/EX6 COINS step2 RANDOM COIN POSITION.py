import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('green')
    fox.draw()
    coin.draw()

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

place_coin()  
pgzrun.go()