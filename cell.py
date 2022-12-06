import pygame
import pygame.draw
x = 0
y = 0
WIDTH = 500
HEIGHT = 500
dif = WIDTH / 9
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
    def get_cell_value(self):
        return self.value
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.note = value
        font = pygame.font.Font(None, 400)
    def draw(self):
        for i in range(2):
            pygame.draw.line(WINDOW, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
            pygame.draw.line(WINDOW, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)
            #pygame.font.SysFont("comicsans", 40)
        #text1 = font1.render(str(val), 1, (0, 0, 0))
        #screen.blit(text1, (x * dif + 15, y * dif + 15))
