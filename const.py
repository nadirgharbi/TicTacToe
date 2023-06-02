import pygame

SIZE = WIDTH, HEIGHT = 650, 525
WIDTH_LINE, HEIGH_LINE = 500, 525

CENTER = 125, 225
DARK = (48, 48, 48)
LIGHT = (213, 209, 213)
RED = (255, 0, 0)
COLOR_O = pygame.Color(35, 157, 184)
COLOR_X = pygame.Color(201, 43, 43)
START_COLOR = pygame.Color(140, 122, 230)

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Tic Tac Toe')
screen.fill(DARK)

# DRAW LINES
horizontal_line1 = (WIDTH//3) + 10
horizontal_line2 = (WIDTH-horizontal_line1) - 10
vertical_line1 = (WIDTH//3) + 10
vertical_line2 = (WIDTH-vertical_line1)
