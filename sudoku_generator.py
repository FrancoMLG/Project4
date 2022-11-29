import pygame
from pygam.locals import *
from constants import *
from cell import Cell



HELLO
screenrect = Rect(0, 0, 287, 287) #SCREEN RESOLUTION WE THINK


WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RED = (255, 0, 0)
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)
CIRCLE_COLOR = (155, 155, 155)
CROSS_COLOR = (66, 66, 66)





class SudokuGenerator:
    def __init__(self, removed_cells, row_length = 9):
        self.row_length = row_length
        self.removed_cells = removed_cells
    def get_board(self):
        pass
    def print_board(self):
        pass
    def valid_in_row(self, row, num):
        self.row = row
        self.num = num
        pass
    def valid_in_col(self, col, num):
        self.col = col
        self.num = num
        pass
    def valid_in_box(self, row_start, col_start, num):
        self.num = num
        self.row_start = row_start
        self.col_start = col_start
        return
    def is_valid(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num

    def fill_box(self, row_start, col_start):
        self.row_start = row_start
        self.col_start = col_start
        pass
    def fill_diagonal(self):
        pass
    def fill_remaining(self, row, col):
        self.row = row
        self.col = col
        pass
    def fill_values(self):
        pass
    def remove_cells(self):
        pass
    def generate_sudoku(size, removed):

        pass

class Cell:
    def __init__(self, value, row, col, screen):
        pass
    def set_cell_value(self, value):
        pass
    def set_sketched_value(self, value):
        pass
    def draw(self):
        pass

class Board:
    def __init__(self, width, height, screen, difficulty):
        pass
    def daw(self):
        pass
    def select(self, row, col):
        pass
    def click(self, x, y):
        pass
    def clear(self):
        game_continue = False
        pass
    def sketch(self, value):
        pass
    def place_number(self, value):
        #place numbers will be sent to check board
        pass
    def reset_to_original(self):
        # check_board is called to reset board
        pass
    def is_full(self):
        # returns a value to the check_board
        # checks the board square is full which gets called to check_board
        pass
    def update_board(self):
        #updates values from player input
        pass
    def find_empty(self):
        # I think this calls for
        pass
    def check_board(self):
        # this checks for that varibles
        # if player wins = game_continue False
        # if player loses = game_continue False but player is able to restart

        pass
