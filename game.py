import pgzrun
from random import randint

apple = Actor("apple")

def draw():
	screen.clear()
	apple.draw()

def place_apple():
	apple.x = randint(10, 800)
	apple.y = randint(10, 600)

def on_mouse_down(pos):
	if apple.collidepoint(pos):
		draw2()
		place_apple()
	else:
		draw3()
		quit()
def draw2():
	screen.draw.text("Nice!", center=(500,500))
def draw3():
	screen.draw.text("Nice!", center=(500,500))
place_apple()
pgzrun.go()
