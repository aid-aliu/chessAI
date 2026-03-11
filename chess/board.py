class Board:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

        self.pawn = 1
        self.rook = 2
        self.knight = 3
        self.bishop = 4
        self.king = 5
        self.queen = 6

        #black turn is when white_turn is false
        self.white_turn = True

        # pawns
        for i in range(8):
            self.board[1][i] = -self.pawn
            self.board[6][i] = self.pawn

        # rooks
        self.board[0][0], self.board[0][7] = -self.rook, -self.rook
        self.board[7][0], self.board[7][7] = self.rook, self.rook

        # knights
        self.board[0][1], self.board[0][6] = -self.knight, -self.knight
        self.board[7][1], self.board[7][6] = self.knight, self.knight

        # bishops
        self.board[0][2], self.board[0][5] = -self.bishop, -self.bishop
        self.board[7][2], self.board[7][5] = self.bishop, self.bishop

        # queens
        self.board[0][3] = -self.queen
        self.board[7][3] = self.queen

        # kings
        self.board[0][4] = -self.king
        self.board[7][4] = self.king


    def print_board(self):
        for i in range(8):
            print(self.board[i])


    # Main controller: validates the move, executes it if allowed, and switches turns
    def try_move(self, row, col, row_move, col_move):

        if self.invalid_move_input(row, col, row_move, col_move):
            return False

        if self.valid_turn_and_target(row, col, row_move, col_move) and self.piece_type_valid_move(row, col, row_move, col_move):
            self.move_piece(row, col, row_move, col_move)

            #switch turns
            if self.white_turn:
                self.white_turn = False
            else:
                self.white_turn = True
            return True

        return False


    # Validates basic move input: ensures coordinates are on the board and source square contains a piece.
    def invalid_move_input(self, row, col, row_move, col_move):

        if row < 0 or row >= 8 or col < 0 or col >= 8:
            print("Position out of bounds")
            return True
        if row_move < 0 or row_move >= 8 or col_move < 0 or col_move >= 8:
            print("Position out of bounds")
            return True

        if self.board[row][col] == 0:
            print("There is no piece located in that position")
            return True

        return False

    # Verifies the piece belongs to the player whose turn it is and the target square is not occupied by the same color.
    def valid_turn_and_target(self, row, col, row_move, col_move):
        if (self.board[row][col] > 0 >= self.board[row_move][col_move]
                and self.white_turn):
            return True

        elif (self.board[row][col] < 0 <= self.board[row_move][col_move]
              and not self.white_turn):
            return True

        return False

    # Updates the board by moving the piece from the source square to the destination square.
    def move_piece(self, row, col, row_move, col_move):
        temp = self.board[row][col]
        self.board[row_move][col_move] = temp
        self.board[row][col] = 0



    # Checks if the requested move follows valid knight movement rules.
    def can_knight(self, row, col, row_move, col_move):

        if row_move == row + 1 or row_move == row - 1:
            if col_move == col + 2 or col_move == col - 2:
                return True
        elif col_move == col + 1 or col_move == col - 1:
            if row_move == row + 2 or row_move == row - 2:
                return True

        return False



    # Checks if the requested move follows valid rook movement rules.
    def can_rook(self, row, col, row_move, col_move):


        i = 0

        if row == row_move and col != col_move:
            distance = col_move - col

            if i < distance:
                i = 1
                while i <= distance - 1:
                    if self.board[row][col + i] != 0:
                        return False
                    i += 1
            elif i > distance:
                i = -1
                while i >= distance + 1:
                    if self.board[row][col + i] != 0:
                        return False
                    i -= 1

            return True

        elif col == col_move and row != row_move:
            distance = row_move - row

            if i < distance:
                i = 1
                while i <= distance - 1:
                    if self.board[row + i][col] != 0:
                        return False
                    i += 1
            elif i > distance:
                i = -1
                while i >= distance + 1:
                    if self.board[row + i][col] != 0:
                        return False
                    i -= 1

            return True

        return False

    def can_bishop(self, row, col, row_move, col_move):

        #check diagonal
        if abs(row_move - row) != abs(col_move - col):
            return False

        i = 0
        distance = row_move - row

        if col_move < col:

            if i > distance:
                i = -1

                while i >= distance + 1:
                    if self.board[row + i][col + i] != 0:
                        return False
                    i -= 1
            elif i < distance:
                i = 1

                while i <= distance - 1:
                    if self.board[row + i][col - i] != 0:
                        return False
                    i += 1
            return True

        elif col_move > col:

            if i > distance:
                i = -1

                while i >= distance + 1:
                    if self.board[row + i][col - i] != 0:
                        return False
                    i -= 1

            elif i < distance:
                i = 1

                while i <= distance - 1:
                    if self.board[row + i][col + i] != 0:
                        return False
                    i += 1
            return True

        return False


    def can_queen(self, row, col, row_move, col_move):
        if self.can_rook(row, col, row_move, col_move) or self.can_bishop(row, col, row_move, col_move):
            return True
        return False

    def can_king(self, row, col, row_move, col_move):

        row_allow = (row_move == row - 1 or row_move == row + 1 or row_move == row)
        col_allow = (col_move == col - 1 or col_move == col + 1 or col_move == col)

        if row_move == row and col_move == col:
            return False
        if row_allow and col_allow:
            return True
        return False

    """self.pawn = 1
        self.rook = 2
        self.knight = 3
        self.bishop = 4
        self.king = 5
        self.queen = 6"""

    def piece_type_valid_move(self, row, col, row_move, col_move):
        if abs(self.board[row][col]) == 2:
            if self.can_rook(row, col, row_move, col_move):
                return True
            return False
        elif abs(self.board[row][col]) == 3:
            if self.can_knight(row, col, row_move, col_move):
                return True
            return False
        elif abs(self.board[row][col]) == 4:
            if self.can_bishop(row, col, row_move, col_move):
                return True
            return False
        elif abs(self.board[row][col]) == 6:
            if self.can_queen(row, col, row_move, col_move):
                return True
            return False
        elif abs(self.board[row][col]) == 5:
            if self.can_king(row, col, row_move, col_move):
                return True
            return False

        return False
