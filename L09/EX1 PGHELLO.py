import pgzrun

WIDTH = 700
HEIGHT = 600

def draw():
    screen.fill((100, 200, 150))
    screen.draw.text('Hello World', topleft=(300, 250), fontsize = 30)

pgzrun.go()