import pygame
import pygame.draw
from cell import Cell
x = 0
y = 0
WIDTH = 500
HEIGHT = 500
dif = WIDTH / 9
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
smallfont = pygame.font.SysFont('Times New Roman', 25)
class Board:
    def __init__(self, width, height, screen, difficulty):
        #Difficulty is equal to the removed cells from the board.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = []
        self.original_board = []
        self.solved_board = []
        #Store original board in self.original_board and do NOT modify.
        #Call fill_values method from SG to construct the board initially.
        for i in range(0, 9):
            self.column_list = []
            for j in range(0, 9):
                cell = Cell(None, i, j, self.screen)
                self.column_list.append(cell)
            self.cells.append(self.column_list)
    def get_board_values(self):
        values = []
        for i in range(0, 9):
            row = self.cells[i]
            col = []
            for j in range(0, 9):
                cell = row[j]
                col.append(cell.get_cell_value())
            values.append(col)
        return values
    def draw(self):
        pass
        for i in range(9):
            for j in range(9):
                if self.screen[i][j] != 0:
                    pygame.draw.rect(WINDOW, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                    text1 = smallfont.render(str(self.screen[i][j]), True, (0, 0, 0))
                    WINDOW.blit(text1, (i * dif + 15, j * dif + 15))
        for i in range(10):
            if i % 3 ==0:
                thickness = 7
            else:
                thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * dif), (500, i * dif), thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thickness)
    def select(self, row, col):
        self.row = row
        self.col = col
        self.current_cell = self.cells[self.row][self.col]
    def click(self, x, y):
        #Calculates the row and column based off the dimensions of the window
        #Call the select method and return a tuple
        pass
    def clear(self):
        for i in range(0, 9):
            current_row = self.cells[i]
            for j in range(0, 9):
                cell = current_row[j]
                cell.set_cell_value(None)
                cell.set_sketched_value(None)
    def sketch(self, value):
        self.current_cell.set_sketched_value(value)
    def place_number(self, value):
        #place numbers will be sent to check board
        self.current_cell.set_cell_value(value)
        #Call this method in SudokuGenerator (press Enter)
    def reset_to_original(self):
        # check_board is called to reset board
        self.cells = self.original_board.copy()
    def is_full(self):
        # returns a value to the check_board
        # checks the board square is full which gets called to check_board
        for i in range(0, 9):
            row = self.cells[i]
            for j in range(0, 9):
                cell = row[j]
                if cell.value == None:
                    return False
        return True
    def update_board(self):
        #updates values from player input
        #Retreive all the numbers from board and update self.cells.
        pass
    def find_empty(self):
        # I think this calls for
        for i in range(0, 9):
            row = self.cells[i]
            for j in range(0, 9):
                cell = row[j]
                if cell.value == None:
                    return (i, j)
    def check_board(self):
        # this checks for that varibles
        # if player wins = game_continue False
        # if player loses = game_continue False but player is able to restart
        for i in range(0, 9):
            row = self.cells[i]
            solved_row = self.solved_board[i]
            for j in range(0, 9):
                cell = row[j]
                solved_cell = solved_row[j]
                if cell.value != solved_cell.value:
                    return False
        return True
