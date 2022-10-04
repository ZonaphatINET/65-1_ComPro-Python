import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600

score = 0

fox = Actor('fox')
fox.pos = 100, 100
coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('green')
    fox.draw()
    coin.draw()
    screen.draw.text('Score : '+str(score), color='white',topleft=(10,10))

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1

update()
pgzrun.go()