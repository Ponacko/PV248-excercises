from random import randint

import pygame
from pygame import display, draw, time, event


class circle:
    def __init__(self):
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.center = [randint(0, 800), randint(0, 600)]
        self.radius = 1
        self.maxr = randint(20, 100)


screen = display.set_mode([800, 600])
clock = time.Clock()
drops = []
while True:
    screen.fill([0, 0, 0])
    for d in drops[:]:
        draw.circle(screen, d.color, d.center, d.radius, 1)
        d.radius += 1
        if d.radius >= d.maxr: drops.remove(d)
    drops.append(circle())
    display.flip()
    clock.tick(60)
    if event.poll().type == pygame.KEYDOWN: break
