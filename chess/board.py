class Board:
    def __init__(self):
        self.chess_board = [[0 for i in range(8)] for j in range(8)]

        self.pawn = 1
        self.rook = 2
        self.knight = 3
        self.bishop = 4
        self.king = 5
        self.queen = 6

        # pawns
        for i in range(8):
            self.chess_board[1][i] = -self.pawn
            self.chess_board[6][i] = self.pawn

        # rooks
        self.chess_board[0][0], self.chess_board[0][7] = -self.rook, -self.rook
        self.chess_board[7][0], self.chess_board[7][7] = self.rook, self.rook

        # knights
        self.chess_board[0][1], self.chess_board[0][6] = -self.knight, -self.knight
        self.chess_board[7][1], self.chess_board[7][6] = self.knight, self.knight

        # bishops
        self.chess_board[0][2], self.chess_board[0][5] = -self.bishop, -self.bishop
        self.chess_board[7][2], self.chess_board[7][5] = self.bishop, self.bishop

        # queens
        self.chess_board[0][3] = -self.queen
        self.chess_board[7][3] = self.queen

        # kings
        self.chess_board[0][4] = -self.king
        self.chess_board[7][4] = self.king

    def print_board(self):
        for i in range(8):
            print(self.chess_board[i])



