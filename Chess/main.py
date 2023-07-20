import pygame

from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (600,600)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])

def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update


if __name__ == '__main__':
    running = True 
    while running: