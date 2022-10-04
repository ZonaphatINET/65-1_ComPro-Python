import pgzrun

WIDTH = 640
HEIGHT = 480

apple = Actor('apple.png')

def draw():
    screen.clear
    apple.draw()

pgzrun.go()