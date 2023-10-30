import sys, pygame
from const import *

# TODO : Faire un systeme de pile pour l'historique de victoire
# TODO : Faire la partie options et quit (GUI)

pygame.init()


class Game:
    def __init__(self):
        # ROUND AND CROSS PLAYER OBJECT
        self.round_img = pygame.image.load('round.png')
        self.cross_img = pygame.image.load('cross.png')

        # 3x3 LINES TO DRAW
        self.horizontal_line1 = (WIDTH_LINE // 3) + 15
        self.horizontal_line2 = (WIDTH_LINE - self.horizontal_line1) - 10
        self.vertical_line1 = (WIDTH_LINE // 3) + 15
        self.vertical_line2 = (WIDTH_LINE - self.vertical_line1) - 10

        # DISPLAY GUI
        self.display_gui = True

        # DISPLAY THE GAME AFTER DISPLAYING THE GUI
        self.display_game = False

        # PLAYER TURNS --> TRUE = O // FALSE = CROSS
        self.turn = True

        # PLAYERS SCORES
        self.score_O = 0
        self.score_X = 0

        # CHECK EMPTY CASES
        self.cases = [
            True, True, True,
            True, True, True,
            True, True, True
        ]

        # CHECK WIN
        self.checkWin = [
            '-', '&', 'é',
            '=', '(', '.',
            'è', '_', 'ç'
        ]

        # FONT
        self.font = pygame.font.Font('freesansbold.ttf', 18)

        # WINS HISTORY
        self.history_win = []

        # WIN MESSAGE TO STRING CHARACTERS
        self.get_win_O = 'PLAYER O gagne !'
        self.get_win_X = 'PLAYER X gagne !'
        self.get_draw = 'Match Nul !'

        # WIN MESSAGE DISPLAY TO SCREEN
        self.messageWin_Player_O = self.font.render(self.get_win_O, True, COLOR_O, DARK)
        self.messageWin_Player_X = self.font.render(self.get_win_X, True, COLOR_X, DARK)
        self.messageDraw = self.font.render(self.get_draw, True, LIGHT, DARK)

        # INIT AND NEW POSITION MESSAGES
        self.init_pos_message_win = 75
        self.new_pos_message_win = self.init_pos_message_win
        self.get_pos_message = []

    def draw_lines(self):
        # HORIZONTAL LINES
        pygame.draw.line(screen, LIGHT, (self.horizontal_line1, 50), (self.horizontal_line1, 430), width=5)
        pygame.draw.line(screen, LIGHT, (self.horizontal_line2, 50), (self.horizontal_line2, 430), width=5)
        # VERTICAL LINES
        pygame.draw.line(screen, LIGHT, (50, self.vertical_line1), (430, self.vertical_line1), width=5)
        pygame.draw.line(screen, LIGHT, (50, self.vertical_line2), (430, self.vertical_line2), width=5)
        # HORIZONTAL TOP / BOTTOM
        pygame.draw.line(screen, LIGHT, (50, 50), (430, 50), width=5)
        pygame.draw.line(screen, LIGHT, (50, 430), (430, 430), width=5)
        # VERTICAL LEFT / RIGHT
        pygame.draw.line(screen, LIGHT, (50, 50), (50, 430), width=5)
        pygame.draw.line(screen, LIGHT, (430, 50), (430, 430), width=5)

    def round(self):
        if self.turn:
            # RIGHT COLUMN
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.cases[8]:  # CASE_9
                    screen.blit(self.round_img, (330, 330))
                    self.cases[8] = False
                    self.checkWin[8] = 'O'

                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[5]:  # CASE_6
                    screen.blit(self.round_img, (330, 205))
                    self.cases[5] = False
                    self.checkWin[5] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[2]:  # CASE_3
                    screen.blit(self.round_img, (330, 75))
                    self.cases[2] = False
                    self.checkWin[2] = 'O'
                    self.turn = False

            # MIDDLE COLUMN
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.cases[7]:  # CASE_8
                    screen.blit(self.round_img, (205, 330))
                    self.cases[7] = False
                    self.checkWin[7] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[4]:  # CASE_5
                    screen.blit(self.round_img, (205, 205))
                    self.cases[4] = False
                    self.checkWin[4] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[1]:  # CASE_2
                    screen.blit(self.round_img, (205, 75))
                    self.cases[1] = False
                    self.checkWin[1] = 'O'
                    self.turn = False

            # LEFT COLUMN
            if 50 < set_pos_mouse_x < 160:
                if (330 < set_pos_mouse_y < 420) and self.cases[6]:  # CASE_7
                    screen.blit(self.round_img, (75, 330))
                    self.cases[6] = False
                    self.checkWin[6] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.cases[3]:  # CASE_4
                    screen.blit(self.round_img, (75, 205))
                    self.cases[3] = False
                    self.checkWin[3] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.cases[0]:  # CASE_1
                    screen.blit(self.round_img, (75, 75))
                    self.cases[0] = False
                    self.checkWin[0] = 'O'
                    self.turn = False

    def cross(self):
        if not self.turn:
            # RIGHT COLUMN
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.cases[8]:  # CASE_9
                    screen.blit(self.cross_img, (330, 330))
                    self.cases[8] = False
                    self.checkWin[8] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.cases[5]:  # CASE_6
                    screen.blit(self.cross_img, (330, 205))
                    self.cases[5] = False
                    self.checkWin[5] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.cases[2]:  # CASE_3
                    screen.blit(self.cross_img, (330, 75))
                    self.cases[2] = False
                    self.checkWin[2] = 'X'
                    self.turn = True

            # MIDDLE COLUMN
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.cases[7]:  # CASE_8
                    screen.blit(self.cross_img, (205, 330))
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

            # LEFT COLUMN
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
        self.gridComplete = all((case == self.cases[0] and case == False) for case in self.cases)

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

        self.history_win.append(self.messageDraw)

    def update_score(self):
        if self.win():
            if not self.turn:
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

                self.history_win.append(self.messageWin_Player_O)

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

                self.history_win.append(self.messageWin_Player_X)

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

    def get_history(self):
        screen.blit(self.history_win[-1], (465, self.init_pos_message_win))


game = Game()

font = pygame.font.Font('freesansbold.ttf', 18)

while True:

    # SET MOUSE
    pos_mouse = pygame.mouse.get_pos()
    set_pos_mouse_x = pos_mouse[0]
    set_pos_mouse_y = pos_mouse[1]
    keypress = pygame.key.get_pressed()

    # WRITE FONTS
    player_X = font.render(f'PLAYER X : {game.score_X}', True, LIGHT, DARK)
    player_O = font.render(f'PLAYER O : {game.score_O}', True, LIGHT, DARK)
    space_message = font.render('TO RESET', True, LIGHT, DARK)
    escape_message = font.render('TO ESCAPE', True, LIGHT, DARK)

    # WRITE TITLE SCREEN
    tic_span = pygame.font.Font('freesansbold.ttf', 52).render('Tic', True, COLOR_O)
    tac_span = pygame.font.Font('freesansbold.ttf', 52).render('Tac', True, COLOR_X)
    toe_span = pygame.font.Font('freesansbold.ttf', 52).render('Toe', True, COLOR_O)

    # IMAGES
    space_image = pygame.image.load('SimpleFlatKeys/Light/Space-Key.png')
    enter_image = pygame.image.load('SimpleFlatKeys/Light/Enter-Key.png')
    start_button = pygame.image.load('assets/start.png')
    options_button = pygame.image.load('assets/options.png')
    quit_button = pygame.image.load('assets/quit.png')

    # SCALE IMAGES
    space_image = pygame.transform.scale(space_image, (78, 34))
    enter_image = pygame.transform.scale(enter_image, (64, 34))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keypress[pygame.K_RETURN]:
            pygame.quit()
            sys.exit()

        if game.display_game:
            game.draw_lines()

            # SET CURSOR FOR PLAYER O AND X
            if game.turn:
                ms_skin = pygame.transform.scale(game.round_img, (22, 22))
                cursor = pygame.cursors.Cursor((2, 2), ms_skin)
                pygame.mouse.set_cursor(cursor)
            elif not game.turn:
                ms_skin = pygame.transform.scale(game.cross_img, (22, 22))
                cursor = pygame.cursors.Cursor((2, 2), ms_skin)
                pygame.mouse.set_cursor(cursor)

            if keypress[pygame.K_SPACE]:
                game.reset_score()
                game.end_game()
                screen.fill(DARK)
                game.draw_lines()

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
                    game.get_history()

                if game.draw_condition():
                    game.update_score()
                    game.end_game()
                    screen.fill(DARK)
                    game.draw_lines()

            # BLIT SCORES PLAYERS
            screen.blit(player_X, (80, 20))
            screen.blit(player_O, (300, 20))
            # BLIT KEY IMAGES AND TEXT
            screen.blit(space_image, (65, 460))
            screen.blit(space_message, (158, 465))
            screen.blit(enter_image, (262, 460))
            screen.blit(escape_message, (341, 465))

        elif not game.display_game:

            # CURSOR IF NOT IN GAME
            ms_skin = pygame.image.load('assets/cursor_default.png')
            ms_skin = pygame.transform.scale(ms_skin, (16, 22))
            cursor = pygame.cursors.Cursor((1, 1), ms_skin)
            pygame.mouse.set_cursor(cursor)

            # BLIT TITLE SCREEN
            if game.display_gui:
                screen.blit(tic_span, (200, 90))
                screen.blit(tac_span, (280, 90))
                screen.blit(toe_span, (370, 90))

                screen.blit(start_button, (250, 180))
                screen.blit(options_button, (250, 260))
                screen.blit(quit_button, (250, 340))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 255 < pos_mouse[0] < 395:
                        if 185 < pos_mouse[1] < 225:
                            screen.fill(DARK)
                            game.display_gui = False
                            game.display_game = True

        pygame.display.flip()


