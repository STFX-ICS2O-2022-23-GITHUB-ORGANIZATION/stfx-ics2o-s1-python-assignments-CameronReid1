import pygame
from pygame import display
from pygame import Color
from pygame import Rect
from pygame import draw


# initialize pygame modules
pygame.init()

# dimensions of the window frame
SIZE = (500,500)

# get a surface for graphic display
gameDisplay = display.set_mode(SIZE)
# set background
gameDisplay.fill(Color('cyan2'))
# draw a house bottom
draw.rect(gameDisplay, Color('gold'), Rect(100, 200, 300, 200))
# draw a roof
point1 = (100, 200)
point2 = (400, 200)
point3 = (250, 50)
draw.polygon(gameDisplay, Color('brown4'), [point1, point2, point3])
#draw sun
centerCircle = (50,50)
radius = 50
draw.circle(gameDisplay, Color('chocolate1'), centerCircle, radius)
# draw grass
draw.rect(gameDisplay, Color('chartreuse4'), Rect(0, 400, 500, 100))

# show the gameDisplay
display.flip()

# wait for user input
input("Press enter to exit game")

# Uninitialize pygame
pygame.quit()

# exit python
quit()


