import pygame
import sys, time, pygame
from const import *

pygame.init()

class Game:
    def __init__(self):
        # ROUND AND CROSS OBJ
        self.round_img = pygame.image.load('round.png')
        self.cross_img = pygame.image.load('cross.png')
        # LINE
        self.horizontal_line1 = (WIDTH_LINE // 3) + 15
        self.horizontal_line2 = (WIDTH_LINE - self.horizontal_line1) - 10
        self.vertical_line1 = (WIDTH_LINE // 3) + 15
        self.vertical_line2 = (WIDTH_LINE - self.vertical_line1) - 10
        self.display_score = True
        self.turn = True
        self.score_O = 0
        self.score_X = 0

        self.cases = [
            True, True, True,
            True, True, True,
            True, True, True
        ]

        self.count_falseCase = 0

        self.checkWin = [
            '-','&','é',
            '=','(','.',
            'è','_','ç'
        ]

        self.history_win = []
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.messageWin_Player_O = self.font.render('PLAYER O won', True, LIGHT, DARK)
        self.messageWin_Player_X = self.font.render('PLAYER X won', True, LIGHT, DARK)

    def draw_lines(self):
        # HORIZONTAL LINES
        pygame.draw.line(screen, LIGHT, (self.horizontal_line1, 50), (self.horizontal_line1, 430), width=5)
        pygame.draw.line(screen, LIGHT, (self.horizontal_line2, 50), (self.horizontal_line2, 430), width=5)
        # VERTICAL LINES
        pygame.draw.line(screen, LIGHT, (50, self.vertical_line1), (430, self.vertical_line1), width=5)
        pygame.draw.line(screen, LIGHT, (50, self.vertical_line2), (430, self.vertical_line2), width=5)
        # HORIZONTAL TOP / BOTTOM
        pygame.draw.line(screen, LIGHT, (50, 50), (430,50), width=5)
        pygame.draw.line(screen, LIGHT, (50, 430), (430, 430), width=5)
        # VERTICAL LEFT / RIGHT
        pygame.draw.line(screen, LIGHT, (50, 50), (50, 430), width=5)
        pygame.draw.line(screen, LIGHT, (430, 50), (430, 430), width=5)

    def round(self):
        if self.turn:
            # RANGEE DROITE
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.cases[8]: # CASE_9
                    screen.blit(self.round_img, (330,330))
                    self.cases[8] = False
                    self.checkWin[8] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[5]: # CASE_6
                    screen.blit(self.round_img, (330, 205))
                    self.cases[5] = False
                    self.checkWin[5] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[2]: # CASE_3
                    screen.blit(self.round_img, (330, 75))
                    self.cases[2] = False
                    self.checkWin[2] = 'O'

                    self.turn = False
            # RANGEE MILIEU
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.cases[7]: # CASE_8
                    screen.blit(self.round_img, (205, 330))
                    self.cases[7] = False
                    self.checkWin[7] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[4]: # CASE_5
                    screen.blit(self.round_img, (205, 205))
                    self.cases[4] = False
                    self.checkWin[4] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[1]: # CASE_2
                    screen.blit(self.round_img, (205, 75))
                    self.cases[1] = False
                    self.checkWin[1] = 'O'
                    self.turn = False

            # RANGEE GAUCHE
            if 50 < set_pos_mouse_x < 160:
                if (330 < set_pos_mouse_y < 420) and self.cases[6]: # CASE_7
                    screen.blit(self.round_img, (75, 330))
                    self.cases[6] = False
                    self.checkWin[6] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[3]: # CASE_4
                    screen.blit(self.round_img, (75, 205))
                    self.cases[3] = False
                    self.checkWin[3] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[0]: # CASE_1
                    screen.blit(self.round_img, (75, 75))
                    self.cases[0] = False
                    self.checkWin[0] = 'O'
                    self.turn = False

    def cross(self):
        if not self.turn:
            # RANGEE DROITE
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.cases[8]:  # CASE_9
                    screen.blit(self.cross_img, (330,330))
                    self.cases[8] = False
                    self.checkWin[8] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.cases[5]:  # CASE_6
                    screen.blit(self.cross_img, (330,205))
                    self.cases[5] = False
                    self.checkWin[5] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.cases[2]:  # CASE_3
                    screen.blit(self.cross_img, (330, 75))
                    self.cases[2] = False
                    self.checkWin[2] = 'X'
                    self.turn = True

            # RANGEE MILIEU
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.cases[7]:  # CASE_8
                    screen.blit(self.cross_img, (205,330))
                    self.cases[7] = False
                    self.checkWin[7] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.cases[4]:  # CASE_5
                    screen.blit(self.cross_img, (205, 205))
                    self.cases[4] = False
                    self.checkWin[4] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.cases[1]:  # CASE_2
                    screen.blit(self.cross_img, (205, 75))
                    self.cases[1] = False
                    self.checkWin[1] = 'X'
                    self.turn = True

            # RANGEE GAUCHE
            if 50 < set_pos_mouse_x < 160:
                if (330 < set_pos_mouse_y < 420) and self.cases[6]:  # CASE_7
                    screen.blit(self.cross_img, (75, 330))
                    self.cases[6] = False
                    self.checkWin[6] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.cases[3]:  # CASE_4
                    screen.blit(self.cross_img, (75, 205))
                    self.cases[3] = False
                    self.checkWin[3] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.cases[0]:  # CASE_1
                    screen.blit(self.cross_img, (75, 75))
                    self.cases[0] = False
                    self.checkWin[0] = 'X'
                    self.turn = True

    def win(self):
        # VERTICAL
        if self.checkWin[0] == self.checkWin[3] == self.checkWin[6]:
            return True
        if self.checkWin[1] == self.checkWin[4] == self.checkWin[7]:
            return True
        if self.checkWin[2] == self.checkWin[5] == self.checkWin[8]:
            return True
        # DIAGONAL
        if self.checkWin[0] == self.checkWin[4] == self.checkWin[8]:
            return True
        if self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
            return True
        # HORIZONTAL
        if self.checkWin[0] == self.checkWin[1] == self.checkWin[2]:
            return True
        if self.checkWin[3] == self.checkWin[4] == self.checkWin[5]:
            return True
        if self.checkWin[6] == self.checkWin[7] == self.checkWin[8]:
            return True

    def draw_condition(self):
        self.gridComplete = all((case == game.cases[0] and case == False) for case in game.cases)
        if self.gridComplete:

            # VERTICAL 0-3-6
            if self.checkWin[0] == self.checkWin[3]:
                if self.checkWin[6] != self.checkWin[0]:
                    return True
                else:
                    return False
            elif self.checkWin[6] == self.checkWin[3]:
                if self.checkWin[0] != self.checkWin[3]:
                    return True
                else:
                    return False

            # VERTICAL 1-4-7
            elif self.checkWin[1] == self.checkWin[4]:
                if self.checkWin[7] != self.checkWin[4]:
                    return True
                else:
                    return False

            elif self.checkWin[7] == self.checkWin[4]:
                if self.checkWin[1] != self.checkWin[4]:
                    return True
                else:
                    return False

            # VERTICAL 2-5-8
            elif self.checkWin[2] == self.checkWin[5]:
                if self.checkWin[8] != self.checkWin[5]:
                    return True
                else:
                    return False

            elif self.checkWin[8] == self.checkWin[5]:
                if self.checkWin[2] != self.checkWin[5]:
                    return True
                else:
                    return False

            # HORIZONTAL 0-1-2
            elif self.checkWin[0] == self.checkWin[1]:
                if self.checkWin[2] != self.checkWin[1]:
                    return True
                else:
                    return False

            elif self.checkWin[2] == self.checkWin[1]:
                if self.checkWin[0] != self.checkWin[1]:
                    return True
                else:
                    return False

            # HORIZONTAL 3-4-5
            elif self.checkWin[3] == self.checkWin[4]:
                if self.checkWin[5] != self.checkWin[4]:
                    return True
                else:
                    return False

            elif self.checkWin[5] == self.checkWin[4]:
                if self.checkWin[3] != self.checkWin[4]:
                    return True
                else:
                    return False

            # HORIZONTAL 6-7-8
            elif self.checkWin[6] == self.checkWin[7]:
                if self.checkWin[8] != self.checkWin[7]:
                    return True
                else:
                    return False

            elif self.checkWin[8] == self.checkWin[7]:
                if self.checkWin[6] != self.checkWin[7]:
                    return True
                else:
                    return False

            # DIAGONAL 0-4-8
            elif self.checkWin[0] == self.checkWin[4]:
                if self.checkWin[8] != self.checkWin[4]:
                    return True
                else:
                    return False

            elif self.checkWin[8] == self.checkWin[4]:
                if self.checkWin[0] != self.checkWin[4]:
                    return True
                else:
                    return False

            # DIAGONAL 2-4-6
            elif self.checkWin[2] == self.checkWin[4]:
                if self.checkWin[6] != self.checkWin[4]:
                    return True
                else:
                    return False

            elif self.checkWin[6] == self.checkWin[4]:
                if self.checkWin[2] != self.checkWin[4]:
                    return True
                else:
                    return False

            else:
                return False

    def update_score(self):
        if self.win():
            if not self.turn:
                self.history_win.append(self.messageWin_Player_O)
                # CIRCLE SCORE VERTICAL
                if (self.checkWin[0] and self.checkWin[3] and self.checkWin[6]) == 'O':
                    self.score_O += 1
                elif (self.checkWin[1] and self.checkWin[4] and self.checkWin[7]) == 'O':
                    self.score_O += 1
                elif (self.checkWin[2] and self.checkWin[5] and self.checkWin[8]) == 'O':
                    self.score_O += 1

                    # CIRCLE SCORE DIAGONAL
                elif (self.checkWin[0] == self.checkWin[4] == self.checkWin[8]) == 'O':
                    self.score_O += 1
                elif self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
                    self.score_O += 1

                    # CIRCLE SCORE HORIZONTAL
                elif (self.checkWin[0] and self.checkWin[1] and self.checkWin[2]) == 'O':
                    self.score_O += 1
                elif (self.checkWin[3] and self.checkWin[4] and self.checkWin[5]) == 'O':
                    self.score_O += 1
                elif (self.checkWin[6] and self.checkWin[7] and self.checkWin[8]) == 'O':
                    self.score_O += 1


            elif self.turn:
                    # CROSS SCORE VERTICAL
                if (self.checkWin[0] and self.checkWin[3] and self.checkWin[6]) == 'X':
                    self.score_X += 1
                elif (self.checkWin[1] and self.checkWin[4] and self.checkWin[7]) == 'X':
                    self.score_X += 1
                elif (self.checkWin[2] and self.checkWin[5] and self.checkWin[8]) == 'X':
                    self.score_X += 1

                    # CROSS SCORE DIAGONAL
                elif (self.checkWin[0] == self.checkWin[4] == self.checkWin[8]) == 'X':
                    self.score_X += 1
                elif self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
                    self.score_X += 1

                    # CROSS SCORE HORIZONTAL
                elif (self.checkWin[0] and self.checkWin[1] and self.checkWin[2]) == 'X':
                    self.score_X += 1
                elif (self.checkWin[3] and self.checkWin[4] and self.checkWin[5]) == 'X':
                    self.score_X += 1
                elif (self.checkWin[6] and self.checkWin[7] and self.checkWin[8]) == 'X':
                    self.score_X += 1

    def reset_stats(self):

        self.cases = [
            True, True, True,
            True, True, True,
            True, True, True]

        self.checkWin = [
            '-', '&', 'é',
            '=', '(', '.',
            'è', '_', 'ç']

    def end_game(self):
        self.reset_stats()

    def reset_score(self):
        self.score_X = 0
        self.score_O = 0

    def draw_history(self):
        return self.history_win

game = Game()

game.draw_lines()

while True:
    clock.tick()
    player_X = game.font.render(f'PLAYER X : {game.score_X}', True, LIGHT, DARK)
    player_O = game.font.render(f'PLAYER O : {game.score_O}', True, LIGHT, DARK)

    space_image = pygame.image.load('SimpleFlatKeys/Light/Space-Key.png')
    enter_image = pygame.image.load('SimpleFlatKeys/Light/Enter-Key.png')

    space_image = pygame.transform.scale(space_image, (78, 34))
    enter_image = pygame.transform.scale(enter_image, (64, 34))

    space_message = font.render('to reset', True, LIGHT, DARK)
    escape_message = font.render('to escape', True, LIGHT, DARK)

    pos_mouse = pygame.mouse.get_pos()
    set_pos_mouse_x = pos_mouse[0]
    set_pos_mouse_y = pos_mouse[1]
    keypress = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keypress[pygame.K_RETURN]:
            pygame.quit()
            sys.exit()
        if keypress[pygame.K_SPACE]:
            game.reset_score()
            game.end_game()
            screen.fill(DARK)
            game.draw_lines()
            # game.menu()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for case in game.cases:
                if case:
                    game.round()
                    game.cross()

        if game.win():
            game.update_score()
            game.end_game()
            screen.fill(DARK)
            game.draw_lines()
            game.draw_history()

        if game.draw_condition():
            game.update_score()
            game.end_game()
            screen.fill(DARK)
            game.draw_lines()

    screen.blit(player_X, (80,20))
    screen.blit(player_O, (300,20))

    screen.blit(space_image, (65, 460))
    screen.blit(space_message, (158, 465))

    screen.blit(enter_image, (262, 460))
    screen.blit(escape_message, (341, 465))

    pygame.display.flip()

