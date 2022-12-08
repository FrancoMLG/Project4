import pygame
import pygame.draw
from sudoku_generator import *
from cell import *
from board import *

WIDTH = 500
HEIGHT = 550
dif = WIDTH / 9
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def get_difficulty(event):
    difficulty = None
    choice = event
    if choice == 1:
        difficulty = 30
    elif choice == 2:
        difficulty = 40
    elif choice == 3:
        difficulty = 50
    return difficulty


def generate_initial_grid(reset_rect, restart_rect, exit_rect):
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(WINDOW, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(WINDOW, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)
        smallfont = pygame.font.SysFont('Times New Roman', 25)
        reset_text = smallfont.render('reset', True, (255, 255, 255))
        pygame.draw.rect(WINDOW, (255, 165, 0), reset_rect)
        WINDOW.blit(reset_text, (75, 510))

        smallfont = pygame.font.SysFont('Times New Roman', 25)
        restart_text = smallfont.render('restart', True, (255, 255, 255))
        pygame.draw.rect(WINDOW, (255, 165, 0), restart_rect)
        WINDOW.blit(restart_text, (220, 510))

        smallfont = pygame.font.SysFont('Times New Roman', 25)
        exit_text = smallfont.render('exit', True, (255, 255, 255))
        pygame.draw.rect(WINDOW, (255, 165, 0), exit_rect)
        WINDOW.blit(exit_text, (380, 510))


def main():
    j_count = 0
    i_count = 0
    pygame.init()
    pygame.display.set_caption('Sudoku')
    running = True
    background_img = pygame.image.load('sudoku.jpg')
    background_img = pygame.transform.scale(background_img, (500, 550))
    smallfont = pygame.font.SysFont('Times New Roman', 25)
    mediumfont = pygame.font.SysFont('Times New Roman', 50)
    largefont = pygame.font.SysFont('Times New Roman', 55)
    welcome_text = largefont.render('Welcome to Sudoku!', True, (0, 0, 0))
    select_text = mediumfont.render('Select Game Mode:', True, (0, 0, 0))
    easy_text = smallfont.render('EASY', True, (255, 255, 255))
    medium_text = smallfont.render('MEDIUM', True, (255, 255, 255))
    hard_text = smallfont.render('HARD', True, (255, 255, 255))
    rand_txt = smallfont.render('HELLO', True, (255, 255, 255))
    WINDOW.fill((255, 0, 0))
    WINDOW.blit(background_img, (0, 0))
    WINDOW.blit(welcome_text, (16, 70))
    WINDOW.blit(select_text, (55, 320))
    easy_rect = pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(25, 400, 125, 50))
    WINDOW.blit(easy_text, (55, 410))
    medium_rect = pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(190, 400, 125, 50))
    WINDOW.blit(medium_text, (201, 411))
    hard_rect = pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(350, 400, 125, 50))
    WINDOW.blit(hard_text, (378, 411))

    reset_rect = pygame.Rect(50, 505, 100, 45)
    restart_rect = pygame.Rect(200, 505, 100, 45)
    exit_rect = pygame.Rect(350, 505, 100, 45)
    game_rect = pygame.Rect(200, 200, 100, 45)
    game_over_rect = pygame.Rect(200, 200, 100, 45)
    button_rect = pygame.Rect(300, 300, 100, 45)



    def button(button_rect):
        pygame.init()
        pygame.display.set_caption('Sudoku')
        running = True
        smallfont = pygame.font.sysFont('Times New Roman', 25)
        button_text = smallfont.render('YO BOI ', True, (0, 0, 255))
        WINDOW.fill((0, 0, 0))
        pygame.draw.rect(WINDOW, (255, 0, 0), button_rect)
        WINDOW.blit(button_text, (300, 300))




    def Game_Over(game_over_rect):
        pygame.init()
        pygame.display.set_caption('Sudoku')
        running = True
        background_img = pygame.image.load('sudoku.jpg')
        background_img = pygame.transform.scale(background_img, (500, 550))
        largefont = pygame.font.SysFont('Times New Roman', 60)
        game_over_text = largefont.render('Game Over!', True, (0, 0, 0))
        smallfont = pygame.font.SysFont('Times New Roman', 25)
        restart_text = smallfont.render('Restart', True, (255, 255, 255))
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(background_img, (0, 0))
        WINDOW.blit(game_over_text, (120, 100))
        pygame.draw.rect(WINDOW, (255, 165, 0), game_over_rect)
        WINDOW.blit(restart_text, (215, 205))


    def Game_Won(game_rect):
        pygame.init()
        pygame.display.set_caption('Sudoku')
        running = True
        background_img = pygame.image.load('sudoku.jpg')
        background_img = pygame.transform.scale(background_img, (500, 550))
        largefont = pygame.font.SysFont('Times New Roman', 60)
        game_won_text = largefont.render('Game Won!', True, (0, 0, 0))
        smallfont = pygame.font.SysFont('Times New Roman', 25)
        exit_text = smallfont.render('Exit', True, (255, 255, 255))
        WINDOW.fill((0, 0, 0))
        WINDOW.blit(background_img, (0, 0))
        WINDOW.blit(game_won_text, (120, 100))
        pygame.draw.rect(WINDOW, (255, 165, 0), game_rect)
        WINDOW.blit(exit_text, (225, 210))

    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    title_screen = True
    game_screen = False
    game_win = False
    game_fin = False
    game_re = False

    # BOARD =

    while running:
        if not Board.check_board:
            Game_Won(game_rect)
            game_win = True
        '''if Board.is_full and not game_win:
            Game_Over(game_over_rect)'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and easy_rect.collidepoint(event.pos) and title_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    sudoku = generate_sudoku(9, get_difficulty(1))
                    print('easy click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)
                    center = dif / 2
                    num_font = pygame.font.SysFont("Times New Roman", 40)
                    for i in sudoku:
                        for j in i:
                            if j != 0:
                                print_num = num_font.render(str(j), False, (0, 0, 0))

                                WINDOW.blit(print_num, ((j_count * dif) + (center - 8), (i_count * dif) + (center - 20)))
                            j_count = j_count + 1
                        j_count = 0
                        # pygame.display.flip()
                        i_count = i_count + 1
                    title_screen = False
                    game_screen = True

            elif event.type == pygame.MOUSEBUTTONDOWN and medium_rect.collidepoint(event.pos) and title_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    sudoku = generate_sudoku(9, get_difficulty(2))
                    print('medium click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)
                    center = dif / 2
                    num_font = pygame.font.SysFont("Times New Roman", 40)
                    for i in sudoku:
                        for j in i:
                            if j != 0:
                                print_num = num_font.render(str(j), False, (0, 0, 0))

                                WINDOW.blit(print_num,
                                            ((j_count * dif) + (center - 8), (i_count * dif) + (center - 20)))
                            j_count = j_count + 1
                        j_count = 0
                        # pygame.display.flip()
                        i_count = i_count + 1
                        # for i in range(9):
                        #     make_button(at coordinates x, y)
                        #     x += width
                        #     of button
                        #     y += length
                        #     of button
                        #     Write
                        #     9
                        #     of
                        #     these
                        #     lines
                        #     of
                        #     code
                    title_screen = False
                    game_screen = True

            elif event.type == pygame.MOUSEBUTTONDOWN and hard_rect.collidepoint(event.pos) and title_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    sudoku = generate_sudoku(9, get_difficulty(3))
                    print('hard click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)
                    center = dif / 2
                    num_font = pygame.font.SysFont("Times New Roman", 40)
                    for i in sudoku:
                        for j in i:
                            if j != 0:
                                print_num = num_font.render(str(j), False, (0, 0, 0))

                                WINDOW.blit(print_num,
                                            ((j_count * dif) + (center - 8), (i_count * dif) + (center - 20)))
                            j_count = j_count + 1
                        j_count = 0
                        # pygame.display.flip()
                        i_count = i_count + 1
                    title_screen = False
                    game_screen = True

            elif event.type == pygame.MOUSEBUTTONDOWN and reset_rect.collidepoint(event.pos) and game_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    print('reset', event.pos)
                    WINDOW.fill((255, 255, 255))
                    game_screen = False
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)




                    # Game_Over(game_over_rect)
                    # playing_board = original board
                    # display playing board

            elif event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos) and game_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    print('restart', event.pos)
                    WINDOW.fill((255, 255, 255))
                    game_screen = False
                    main()
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos) and game_screen:
                if pygame.mouse.get_pressed()[0] == 1:
                    print('EXIT', event.pos)
                    # WINDOW.fill((255, 255, 255))
                    game_screen = False
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and game_over_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('COMEBACK', event.pos)
                    WINDOW.fill((255, 255, 255))
                    main()
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and game_rect.collidepoint(event.pos) and game_win:
                if pygame.mouse.get_pressed()[0] == 1:
                    print('QUIT', event.pos)
                    WINDOW.fill((255, 255, 255))
                    running = False


            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('num', event.pos)
                    WINDOW.fill((255, 255, 255))


        pygame.display.update()

    # pygame.quit()


if __name__ == '__main__':
    main()
