from sudoku_generator import SudokuGenerator, Cell, Board
import pygame

pygame.init()
WIDTH = 500
HEIGHT = 500
dif = WIDTH / 9
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
run = True
background_img = pygame.image.load('sudoku.jpg')
background_img = pygame.transform.scale(background_img, (500, 500))
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

if __name__ == '__main__':
    pass
