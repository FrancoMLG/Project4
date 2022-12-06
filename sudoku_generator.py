import pygame
import pygame.draw
import random
x = 0
y = 0
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
    pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(25, 400, 125, 50))
    WINDOW.blit(easy_text, (55, 410))
    pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(190, 400, 125, 50))
    WINDOW.blit(medium_text, (201, 411))
    pygame.draw.rect(WINDOW, (255, 165, 0), pygame.Rect(350, 400, 125, 50))
    WINDOW.blit(hard_text, (378, 411))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#pygame.quit()
def generate_sudoku(size, removed):
    pass
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
class SudokuGenerator:
    def __init__(self, removed_cells, row_length=9):
        self.boardobject = Board(9, WIDTH, HEIGHT, 30)
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = self.get_board()
        self.box_length = 3
    def get_board(self):
        return self.board.get_board_values()
        # board = [["-" for i in range(self.row_length)] for j in range(self.row_length)]
        # return board
    def print_board(self):
        board = self.get_board()
        for i in range(0, 9):
            row = board[i]
            print(row)
            print()
        # board = self.get_board
        # for row in board:
        # for col in row:
        # print(col, end= '')
        # print()
    def valid_in_row(self, row, num):
        if not isinstance(row, int):  # row is int
            return False
        if not isinstance(num, int):  # num is int
            return False
        if num < 1 or num > 9:
            return False
        if row >= len(self.board) or row < 0:
            return False
        for col in range(len(self.board[row])):
            if self.board[row][col] == num:
                return False
        return True
    def valid_in_col(self, col, num):
        if not isinstance(col, int):  # row is int
            return False
        if not isinstance(num, int):  # num is int
            return False
        if num < 1 or num > 9:
            return False
        if col >= len(self.board[0]) or col < 0:
            return False
        for row in range(len(self.board)):
            if self.board[row][col] == num:
                return False
        return True
    def valid_in_box(self, row_start, col_start, num):
        if not isinstance(row_start, int):
            return False
        if not isinstance(col_start, int):
            return False
        if not isinstance(num, int):
            return False
        if row_start % 3 != 0 or col_start % 3 != 0:
            return False
        if num < 1 or num > 9:
            return False
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True
    def is_valid(self, row, col, num):
        if not isinstance(row, int):
            return False
        if not isinstance(col, int):
            return False
        if not isinstance(num, int):
            return False
        return self.valid_in_row(row, num) and \
               self.valid_in_col(col, num) and \
               self.valid_in_box(row - row % 3, col - col % 3, num)
    def fill_box(self, row_start, col_start):
        if not isinstance(row_start, int):
            return False
        if not isinstance(col_start, int):
            return False
        row_start -= row_start % 3
        col_start -= col_start % 3
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] != 0:
                    continue
                while True:
                    num = random.randint(1, 9)
                    if self.is_valid(row, col, num):
                        break
                self.board[row][col] = num
    def fill_diagonal(self):
        for pos in range(0, 9, 3):
            self.fill_box(pos, pos)
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    def remove_cells(self):
        removed_cells = []
        index = 1
        while True:
            if index == self.removed_cells:
                break
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if[row, col] in removed_cells:
                continue
            else:
                self.board[row][col] = 0
                removed_cells.append([row, col])
                index += 1

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
        # Draw the lines
        for i in range(9):
            for j in range(9):
                if self.screen[i][j] != 0:
                    pygame.draw.rect(WINDOW, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
                    text1 = smallfont.render(str(self.screen[i][j]), 1, (0, 0, 0))
                    WINDOW.blit(text1, (i * dif + 15, j * dif + 15))
        for i in range(10):
            if i % 3 ==0:
                thick = 7
            else:
                thick = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)
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
