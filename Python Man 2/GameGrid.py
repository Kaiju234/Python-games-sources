import pygame

pygame.init()

WIDTH = 900
HEIGHT = 950 

screen = pygame.display.set_mode([WIDTH,HEIGHT])
timer  = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont('Arial', 20)

run = True
while run:
    timer.tick(fps)
    screen.fill('black')
pass
