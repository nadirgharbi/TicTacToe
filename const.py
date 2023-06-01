""" ICI, LES SIMPLES VARIABLES COMME DES ENTIERS, LISTES, STRING, TUPLES... """
# VARIABLES
import pygame
SIZE = WIDTH, HEIGHT = 600, 525
WIDTH_LINE, HEIGH_LINE = 500, 525

CENTER = 125,225
DARK = (43,43,43)
LIGHT = (213,209,213)
RED = (255,0,0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tic Tac Toe')
screen.fill(DARK)

# DRAW LINES
horizontal_line1 = (WIDTH//3) +10
horizontal_line2 = (WIDTH-horizontal_line1) -10
vertical_line1 = (WIDTH//3) +10
vertical_line2 = (WIDTH-vertical_line1)

size_symbol = 50,50