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
    if game_over:
        screen.fill('pink')
        message = 'Final Score : '+str(score)
        screen.draw.text(message, topleft=(10,10),fontsize=50)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def update():
    global score
    if fox.x == 000:
        fox.x = fox.x = 000

    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x + 5
    elif keyboard.up:
        fox.y = fox.y - 5
    elif keyboard.down:
        fox.y = fox.y + 5


    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        score += 1

game_over = False

def time_up():
    global game_over
    game_over = True


place_coin()
clock.schedule(time_up, 10.0)
pgzrun.go()