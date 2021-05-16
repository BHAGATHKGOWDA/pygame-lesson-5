import pygame, sys, time
from pygame import display, event, draw

pygame.init()
screen = display.set_mode((800, 550))
display.set_caption("My First Game")
r = (255, 0, 0)
x = 0
y = 275
for i in range(1, 15):
    x = x + 50
    rectangle = (x, y, 40, 40)
    draw.rect(screen, r, rectangle)
    display.flip()
    time.sleep(0.5)
while True:
    allevents = event.get()
    for myevent in allevents:
        if myevent.type == pygame.QUIT:
            sys.exit()

    display.flip()
