import pygame
import pygame.draw
from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
WIDTH = 500
HEIGHT = 550
dif = WIDTH / 9
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
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

def reset_game():
    pass


def restart_game():
    pygame.init()
    pygame.display.set_caption('Sudoku')
    running = True
    background_img = pygame.image.load('sudoku.jpg')
    background_img = pygame.transform.scale(background_img, (500, 550))
    WINDOW.fill((0, 0, 0))

def Game_Over(game_rect):
    pygame.init()
    pygame.display.set_caption('Sudoku')
    running = True
    background_img = pygame.image.load('sudoku.jpg')
    background_img = pygame.transform.scale(background_img, (500, 550))
    largefont = pygame.font.SysFont('Times New Roman', 55)
    game_over_text = largefont.render('Game Over!', True, (0, 0, 0))
    smallfont = pygame.font.SysFont('Times New Roman', 25)
    exit_text = smallfont.render('exit', True, (255, 255, 255))
    pygame.draw.rect(WINDOW, (255, 165, 0), game_rect)
    WINDOW.blit(exit_text, (380, 250))
    game_rect = pygame.Rect(350, 505, 100, 45)



def main():
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
    WINDOW.fill((0, 0, 0))
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



    #BOARD =

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and easy_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    #SudokuGenerator = Board()
                    print('easy click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)
                    #pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN and medium_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('medium click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)
            elif event.type == pygame.MOUSEBUTTONDOWN and hard_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('hard click')
                    WINDOW.fill((255, 255, 255))
                    generate_initial_grid(reset_rect, restart_rect, exit_rect)

            elif event.type == pygame.MOUSEBUTTONDOWN and reset_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('reset', event.pos)
                    WINDOW.fill((255, 255, 255))



            elif event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('restart', event.pos)
                    WINDOW.fill((255, 255, 255))

            elif event.type == pygame.MOUSEBUTTONDOWN and exit_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('EXIT', event.pos)
                    WINDOW.fill((255, 255, 255))
                    Game_Over(game_rect)

            elif event.type == pygame.MOUSEBUTTONDOWN and game_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('QUIT', event.pos)
                    WINDOW.fill((255, 255, 255))
                    Game_Over(game_rect)



        pygame.display.update()

    #pygame.quit()


if __name__ == '__main__':
    main()
