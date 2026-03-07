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


    def move_piece(self, row, col, row_move, col_move):

        if row < 0 or row >= 8 or col < 0 or col >= 8:
            print("Position out of bounds")
            return False
        if row_move < 0 or row_move >= 8 or col_move < 0 or col_move >= 8:
            print("Position out of bounds")
            return False


        if (self.board[row][col] > 0 >= self.board[row_move][col_move]
                and self.white_turn):
            temp = self.board[row][col]
            self.board[row_move][col_move] = temp
            self.board[row][col] = 0
            self.white_turn = False
            return True

        elif (self.board[row][col] < 0 <= self.board[row_move][col_move]
              and not self.white_turn):
            temp = self.board[row][col]
            self.board[row_move][col_move] = temp
            self.board[row][col] = 0
            self.white_turn = True
            return True

        return False

