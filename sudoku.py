import pygame
import pygame.draw
from sudoku_generator import SudokuGenerator
from cell import Cell
from board import Board
def main():
    pygame.init()
    WIDTH = 500
    HEIGHT = 500
    dif = WIDTH / 9
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku')
    running = True
    background_img = pygame.image.load('sudoku.jpg')
    background_img = pygame.transform.scale(background_img, (500, 500))
    smallfont = pygame.font.SysFont('Times New Roman', 25)
    mediumfont = pygame.font.SysFont('Times New Roman', 50)
    largefont = pygame.font.SysFont('Times New Roman', 55)
    welcome_text = largefont.render('Welcome to Sudoku!', True, (0, 0, 0))
    select_text = mediumfont.render('Select Game Mode:', True, (0, 0, 0))
    easy_text = smallfont.render('EASY', True, (255, 255, 255))
    medium_text = smallfont.render('MEDIUM', True, (255, 255, 255))
    hard_text = smallfont.render('HARD', True, (255, 255, 255))
    while running:
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
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and easy_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    Board.draw()
            if event.type == pygame.MOUSEBUTTONDOWN and medium_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('medium click')
            if event.type == pygame.MOUSEBUTTONDOWN and hard_rect.collidepoint(event.pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    print('hard click')
    #pygame.quit()

if __name__ == '__main__':
    main()
