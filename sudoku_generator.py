import random
#This function generates a sudoku grid with the number of removed cells depending on the difficulty level.
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
#This class makes a completed sudoku grid and then removes cells for the player to fill.
class SudokuGenerator:
#This function is the constructor and initializes the row length, number of removed cells, box length, and the 2D board
#list.
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.box_length = 3
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(self.row_length)] for j in range(self.row_length)]
#This function essentially just returns 2D board list, a 2D list of numbers.
    def get_board(self):
        return self.board
#This function prints the board and is not required but is useful during the debugging process.
    def print_board(self):
        board = self.get_board()
        for i in range(0, 9):
            row = board[i]
            print(row)
            print()
#This function checks to see if the inputted integer is already in the row or not, if it is it returns False, otherwise
#it reutrns True.
    def valid_in_row(self, row, num):
        for col in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True
#This function checks to see if the inputted integer is already in the column or not, if it is it returns False,
#otherwise it reutrns True.
    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True
#This function checks to see if the inputted integer is already in the box or not, if it is it returns False,
#otherwise it reutrns True.
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
#This function if an inputted integer would be valid in the cell it is inputted based on the return values of the
#previous three functions.
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num)
#This function fills a box by trying a random number from a range of 1-9 and seeing if that number is valid or not.
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
#This function fills the grid diagonally by calling fill_box.
    def fill_diagonal(self):
        for pos in range(0, self.row_length, self.box_length):
            self.fill_box(pos, pos)
#This function fills in the remaining cells using a method called back tracking which is beyond the scope of this class
#hence why this function was provided for us.
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
#This function fills up the board by calling fill_diagonal and fill_remaining.
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
#This function removes cells from a filled sudoku board specified by self.removed_cells.
    def remove_cells(self):
        index = self.removed_cells
        while True:
            if index == 0:
                break
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] == 0:
                continue
            else:
                self.board[row][col] = 0
                index -= 1






