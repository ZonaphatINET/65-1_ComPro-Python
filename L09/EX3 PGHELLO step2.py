from random import randint
import pgzrun

WIDTH = 640
HEIGHT = 480

apple = Actor('apple')

def draw():
    screen.clear
    apple.draw()

def place_apple():
    apple.x = randint(10, 600)
    apple.y = randint(10, 400)

place_apple()    
pgzrun.go()