import sys, pygame, pygame_gui
from const import *
from game import *

# TODO : Faire un systeme de pile pour l'historique de victoire

pygame.init()

game = Game()

font = pygame.font.Font('freesansbold.ttf', 18)

while True:

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
    start_button = pygame.image.load('start.png')
    options_button = pygame.image.load('options.png')
    quit_button = pygame.image.load('quit.png')

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
                ms_skin = pygame.image.load('round.png')
                cursor = pygame.cursors.Cursor((2, 2), ms_skin)
                pygame.mouse.set_cursor(cursor)
            elif not game.turn:
                ms_skin = pygame.image.load('cross.png')
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

        pygame.display.flip()

        # if not(game.display_game):
        #     # BLIT TITLE SCREEN
        #     if game.display_gui:
        #         screen.blit(tic_span, (200, 90))
        #         screen.blit(tac_span, (280, 90))
        #         screen.blit(toe_span, (370, 90))
        #
        #         ms_skin = pygame.image.load('mouse_skin_default.png')
        #         ms_skin = pygame.transform.scale(ms_skin, (16, 22))
        #         cursor = pygame.cursors.Cursor((1, 1), ms_skin)
        #         pygame.mouse.set_cursor(cursor)
        #         screen.blit(start_button, (250, 180))
        #         screen.blit(options_button, (250, 260))
        #         screen.blit(quit_button, (250, 340))
        #         print(pos_mouse)
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             pass
        #             if 255 < pos_mouse[0] < 395:
        #                 if 185 < pos_mouse[1] < 225:
        #                     game.display_game = True
        #                     game.display_gui = False
        #
        # cursor = pygame.cursors.Cursor((2, 2), ms_skin)
        # pygame.mouse.set_cursor(cursor)
