import copy

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

        self.board_previous = copy.deepcopy(self.board)

        if self.invalid_move_input(row, col, row_move, col_move):
            return False

        if self.valid_turn_and_target(row, col, row_move, col_move) and self.piece_type_valid_move(row, col, row_move, col_move):
            self.move_piece(row, col, row_move, col_move)

            # check() is used to test whether the move leaves the current side's king under attack; if yes, the move is illegal
            if self.check():
                self.board = copy.deepcopy(self.board_previous)
                return False

            #check a pawn for promotion
            self.pawn_promotion(row_move, col_move)


            #switch turns
            if self.white_turn:
                self.white_turn = False
            else:
                self.white_turn = True
            return True

        return False




    def is_legal_move(self, row, col, row_move, col_move):

        current_board = copy.deepcopy(self.board)
        current_turn = self.white_turn

        result = self.try_move(row, col, row_move, col_move)

        self.board = current_board
        self.white_turn = current_turn

        return result

    """     pawn = 1
                rook = 2
                knight = 3
                bishop = 4
                king = 5
                queen = 6   """

    def get_legal_moves(self):
        legal_moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]

                if piece == 0:
                    continue
                if self.white_turn and piece < 0:
                    continue
                if not self.white_turn and piece > 0:
                    continue

                piece_type = abs(piece)

                if piece_type == 1:
                    legal_moves.extend(self.generate_pawn_legal_moves(i, j))
                elif piece_type == 2:
                    legal_moves.extend(self.generate_rook_legal_moves(i, j))
                elif piece_type == 3:
                    legal_moves.extend(self.generate_knight_legal_moves(i, j))
                elif piece_type == 4:
                    legal_moves.extend(self.generate_bishop_legal_moves(i, j))
                elif piece_type == 5:
                    legal_moves.extend(self.generate_king_legal_moves(i, j))
                elif piece_type == 6:
                    legal_moves.extend(self.generate_queen_legal_moves(i, j))

        return legal_moves

    def generate_knight_legal_moves(self, row, col):
        knight_legal = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for i, j in knight_moves:
            if self.is_legal_move(row, col, row + i, col + j):
                knight_legal.append((row, col, row + i, col + j))

        return knight_legal

    def generate_king_legal_moves(self, row, col):

        king_legal = []

        king_moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for i, j in king_moves:
            if self.is_legal_move(row, col, row + i, col + j):
                king_legal.append((row, col, row + i, col + j))
        return king_legal

    def generate_bishop_legal_moves(self, row, col):

        bishop_legal = []

        for i in range(1, 8):

            if self.is_legal_move(row, col, row + i, col + i):
                bishop_legal.append((row, col,row + i, col + i))

            if self.is_legal_move(row, col, row + i, col - i):
                bishop_legal.append((row, col,row + i, col - i))

            if self.is_legal_move(row, col, row - i, col + i):
                bishop_legal.append((row, col,row - i, col + i))

            if self.is_legal_move(row, col, row - i, col - i):
                bishop_legal.append((row, col, row - i, col - i))

        return bishop_legal

    def generate_rook_legal_moves(self, row, col):

        rook_legal = []

        for i in range(1, 8):
            if self.is_legal_move(row, col, row, col + i):
                rook_legal.append((row, col, row, col + i))

            if self.is_legal_move(row, col, row, col - i):
                rook_legal.append((row, col, row, col - i))

            if self.is_legal_move(row, col, row - i, col):
                rook_legal.append((row, col, row - i, col))

            if self.is_legal_move(row, col, row + i, col):
                rook_legal.append((row, col, row + i, col))

        return rook_legal


    def generate_queen_legal_moves(self, row, col):
        return self.generate_rook_legal_moves(row, col) + self.generate_bishop_legal_moves(row, col)

    def generate_pawn_legal_moves(self, row, col):

        pawn_legal = []

        if self.board[row][col] == -1 and row == 1:
            if self.is_legal_move(row, col, row + 2, col):
                pawn_legal.append((row, col, row + 2, col))
            if self.is_legal_move(row, col, row + 1, col):
                pawn_legal.append((row, col, row + 1, col))
            if self.is_legal_move(row, col, row + 1, col - 1):
                pawn_legal.append((row, col, row + 1, col - 1))
            if self.is_legal_move(row, col, row + 1, col + 1):
                pawn_legal.append((row, col, row + 1, col + 1))

        elif self.board[row][col] == 1 and row == 6:
            if self.is_legal_move(row, col, row - 2, col):
                pawn_legal.append((row, col, row - 2, col))
            if self.is_legal_move(row, col, row - 1, col):
                pawn_legal.append((row, col, row - 1, col))
            if self.is_legal_move(row, col, row - 1, col - 1):
                pawn_legal.append((row, col, row - 1, col - 1))
            if self.is_legal_move(row, col, row - 1, col + 1):
                pawn_legal.append((row, col, row - 1, col + 1))

        elif self.board[row][col] == -1 and row != 1:
            if self.is_legal_move(row, col, row + 1, col):
                pawn_legal.append((row, col, row + 1, col))
            if self.is_legal_move(row, col, row + 1, col - 1):
                pawn_legal.append((row, col, row + 1, col - 1))
            if self.is_legal_move(row, col, row + 1, col + 1):
                pawn_legal.append((row, col, row + 1, col + 1))

        elif self.board[row][col] == 1 and row != 6:
            if self.is_legal_move(row, col, row - 1, col):
                pawn_legal.append((row, col, row - 1, col))
            if self.is_legal_move(row, col, row - 1, col - 1):
                pawn_legal.append((row, col, row - 1, col - 1))
            if self.is_legal_move(row, col, row - 1, col + 1):
                pawn_legal.append((row, col, row - 1, col + 1))

        return pawn_legal


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


    def can_pawn(self, row, col, row_move, col_move):

        #pawns at the start of the board
        if row == 1 and col_move == col and row_move <= 3 and row_move > 1:
            if row_move == row + 1 and self.board[row_move][col_move] == 0:
                return True
            elif row_move == row + 2 and self.board[row_move][col_move] == 0 and self.board[row + 1][col] == 0:
                return True
            return False
        elif row == 6 and col_move == col and row_move >= 4 and row_move < 6:
            if row_move == row - 1 and self.board[row_move][col_move] == 0:
                return True
            elif row_move == row - 2 and self.board[row - 1][col_move] == 0 and self.board[row_move][col_move] == 0:
                return True
            return False

        #pawns moving 1 block forward
        if row_move == row + 1  and self.board[row][col] == -1 and self.board[row_move][col_move] == 0 and col_move == col:
            return True
        elif row_move == row - 1  and self.board[row][col] == 1 and self.board[row_move][col_move] == 0 and col_move == col:
            return True

        #pawns moving diagonally when taking another piece
        if self.board[row_move][col_move] > 0 and row_move == row + 1 and (col_move == col + 1 or col_move == col - 1):
            return True
        elif self.board[row_move][col_move] < 0 and row_move == row - 1 and (col_move == col + 1 or col_move == col - 1):
            return True

        return False

    def pawn_promotion(self, row_move, col_move):
        if (row_move == 0 and self.board[row_move][col_move] == 1) or (
                row_move == 7 and self.board[row_move][col_move] == -1):
            while True:
                promotion = input("Turn pawn into (2)-rook, (3)-knight, (4)-bishop, (6)-queen")
                if promotion not in ["2", "3", "4", "6"]:
                    print("Invalid input")
                else:
                    if self.board[row_move][col_move] == 1:
                        self.board[row_move][col_move] = int(promotion[0])
                        return True
                    else:
                        self.board[row_move][col_move] = -int(promotion[0])
                        return True




    """
    1. Detect **check**
    2. Reject moves that **leave your king in check**   
    3. Prevent **king moving into check**
    4. Implement **legal move generation for a side**
    5. Detect **checkmate**
    6. Detect **stalemate**
    7. Implement **castling**
    8. Implement **en passant**
    9. Add **move history**
"""


    def piece_type_valid_move(self, row, col, row_move, col_move):
        if abs(self.board[row][col]) == 2:
            if self.can_rook(row, col, row_move, col_move):
                return True
            return False
        elif abs(self.board[row][col]) == 1:
            if self.can_pawn(row, col, row_move, col_move):
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

    """Check methods and check logic implementation"""

    def check(self):
        """nese u bo ni levizje prej tbardhes, kqyre mbretin e zi or vice versa"""
        """kqyre diagnoalisht a po sulomhet mbreti prej naj bishopi ose mbretreshe(rruga prej mbretit te bishopi duhet me kon e paster, so square = 0"""
        """kqyre ne form kryqi njejt per rook ose mbretresh"""
        """kqyre ne diagonalet afer mbretit mos osht pawn"""
        """nese njona prej qytyne plotsohet, dije qe osht check"""
        """per knights as well, edhe kqyre mos e le mbrtin e zi me kon 1 row ose 1 column afer te bardhit, duhet me pas 1 square distance mes dyve gjith"""


        if self.knight_check():
            return True
        elif self.rook_check():
            return True
        elif self.bishop_check():
            return True
        elif self.pawn_check():
            return True
        elif self.king_adjacency_check():
            return True

        return False

        #checks if the white king is checked on it's own turn

    def find_king(self):

        king = 5 if self.white_turn else -5


        for i in range(8):
            for j in range(8):
                if self.board[i][j] == king:
                    king_row = i
                    king_col = j
                    return [king_row, king_col]

    def knight_check(self):
        king_row, king_col = self.find_king()

        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        if self.board[king_row][king_col] == 5:
            for row, column in knight_moves:
                if 0 <= king_row + row < 8 and 0 <= king_col + column < 8:
                    if self.board[king_row + row][king_col + column] == -3:
                        return True
        elif self.board[king_row][king_col] == -5:
            for row, column in knight_moves:
                if 0 <= king_row + row < 8 and 0 <= king_col + column < 8:
                    if self.board[king_row + row][king_col + column] == 3:
                        return True
        return False

    def rook_check(self):

        king_row, king_col = self.find_king()

        val1 = True
        val2 = True
        val3 = True
        val4 = True


        i_down, k_right, j_up, l_left = 1, 1, 1, 1

        if self.board[king_row][king_col] == 5:

            while True:
                # right
                if king_col + k_right < 8 and val1:
                    if self.board[king_row][king_col + k_right] == -2 or self.board[king_row][king_col + k_right] == -6:
                        return True
                    elif self.board[king_row][king_col + k_right] == 0:
                        k_right += 1
                    else:
                        val1 = False

                elif val1:
                    val1 = False

                # left
                if 0 <= king_col - l_left and val2:
                    if self.board[king_row][king_col - l_left] == -2 or self.board[king_row][king_col - l_left] == -6:
                        return True
                    elif self.board[king_row][king_col - l_left] == 0:
                        l_left += 1
                    else:
                        val2 = False

                elif val2:
                    val2 = False

                # down
                if king_row + i_down < 8 and val3:
                    if self.board[king_row + i_down][king_col] == -2 or self.board[king_row + i_down][king_col] == -6:
                        return True
                    elif self.board[king_row + i_down][king_col] == 0:
                        i_down += 1
                    else:
                        val3 = False

                elif val3:
                    val3 = False

                # up
                if 0 <= king_row - j_up and val4:
                    if self.board[king_row - j_up][king_col] == -2 or self.board[king_row - j_up][king_col] == -6:
                        return True
                    elif self.board[king_row - j_up][king_col] == 0:
                        j_up += 1
                    else:
                        val4 = False

                elif val4:
                    val4 = False

                if not val1 and not val2 and not val3 and not val4:
                    return False

        elif self.board[king_row][king_col] == -5:

            while True:
                # right
                if king_col + k_right < 8 and val1:
                    if self.board[king_row][king_col + k_right] == 2 or self.board[king_row][king_col + k_right] == 6:
                        return True
                    elif self.board[king_row][king_col + k_right] == 0:
                        k_right += 1
                    else:
                        val1 = False

                elif val1:
                    val1 = False


                # left
                if 0 <= king_col - l_left and val2:
                    if self.board[king_row][king_col - l_left] == 2 or self.board[king_row][king_col - l_left] == 6:
                        return True
                    elif self.board[king_row][king_col - l_left] == 0:
                        l_left += 1
                    else:
                        val2 = False
                elif val2:
                    val2 = False

                # down
                if king_row + i_down < 8 and val3:
                    if self.board[king_row + i_down][king_col] == 2 or self.board[king_row + i_down][king_col] == 6:
                        return True
                    elif self.board[king_row + i_down][king_col] == 0:
                        i_down += 1
                    else:
                        val3 = False

                elif val3:
                    val3 = False

                # up
                if 0 <= king_row - j_up and val4:
                    if self.board[king_row - j_up][king_col] == 2 or self.board[king_row - j_up][king_col] == 6:
                        return True
                    elif self.board[king_row - j_up][king_col] == 0:
                        j_up += 1
                    else:
                        val4 = False

                elif val4:
                    val4 = False


                if not val1 and not val2 and not val3 and not val4:
                    return False

        return False


    def bishop_check(self):

        king_row, king_col = self.find_king()

        i = 1

        #use 4 seperate loops instead of 1 giant one


        if self.board[king_row][king_col] == -5:
            # right down
            while 0 <= king_row + i < 8 and 0 <= king_col + i < 8:
                if self.board[king_row + i][king_col + i] == 0:
                    i += 1
                    continue
                elif self.board[king_row + i][king_col + i] == 4 or self.board[king_row + i][king_col + i] == 6:
                    return True
                else:
                    break

            i = 1
            # right up
            while 0 <= king_row - i < 8 and 0 <= king_col + i < 8:
                if self.board[king_row - i][king_col + i] == 0:
                    i += 1
                    continue
                elif self.board[king_row - i][king_col + i] == 4 or self.board[king_row - i][king_col + i] == 6:
                    return True
                else:
                    break

            i = 1
            # left up
            while 0 <= king_row - i < 8 and 0 <= king_col - i < 8:
                if self.board[king_row - i][king_col - i] == 0:
                    i += 1
                    continue
                elif self.board[king_row - i][king_col - i] == 4 or self.board[king_row - i][king_col - i] == 6:
                    return True
                else:
                    break

            i = 1
            # left down
            while 0 <= king_row + i < 8 and 0 <= king_col - i < 8:
                if self.board[king_row + i][king_col - i] == 0:
                    i += 1
                    continue
                elif self.board[king_row + i][king_col - i] == 4 or self.board[king_row + i][king_col - i] == 6:
                    return True
                else:
                    break


        elif self.board[king_row][king_col] == 5:

            # right down
            while 0 <= king_row + i < 8 and 0 <= king_col + i < 8:
                if self.board[king_row + i][king_col + i] == 0:
                    i += 1
                    continue
                elif self.board[king_row + i][king_col + i] == -4 or self.board[king_row + i][king_col + i] == -6:
                    return True
                else:
                    break

            i = 1
            # right up
            while 0 <= king_row - i < 8 and 0 <= king_col + i < 8:
                if self.board[king_row - i][king_col + i] == 0:
                    i += 1
                    continue
                elif self.board[king_row - i][king_col + i] == -4 or self.board[king_row - i][king_col + i] == -6:
                    return True
                else:
                    break

            i = 1
            # left up
            while 0 <= king_row - i < 8 and 0 <= king_col - i < 8:
                if self.board[king_row - i][king_col - i] == 0:
                    i += 1
                    continue
                elif self.board[king_row - i][king_col - i] == -4 or self.board[king_row - i][king_col - i] == -6:
                    return True
                else:
                    break

            i = 1
            # left down
            while 0 <= king_row + i < 8 and 0 <= king_col - i < 8:
                if self.board[king_row + i][king_col - i] == 0:
                    i += 1
                    continue
                elif self.board[king_row + i][king_col - i] == -4 or self.board[king_row + i][king_col - i] == -6:
                    return True
                else:
                    break

        return False



    def pawn_check(self):

        king_row, king_col = self.find_king()



        if self.board[king_row][king_col] == -5:
            if 0 <= king_row + 1 < 8:
                if 0 <= king_col + 1 < 8:
                     if self.board[king_row + 1][king_col + 1] == 1:
                        return True
                if 0 <= king_col - 1 < 8:
                     if self.board[king_row + 1][king_col - 1] == 1:
                         return True

        elif self.board[king_row][king_col] == 5:
            if 0 <= king_row - 1 < 8:
                if 0 <= king_col + 1 < 8:
                    if self.board[king_row - 1][king_col + 1] == -1:
                        return True
                if 0 <= king_col - 1 < 8:
                    if self.board[king_row - 1][king_col - 1] == -1:
                        return True

        return False

    def king_adjacency_check(self):

        king_row, king_col = self.find_king()

        king_moves = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        if self.board[king_row][king_col] == -5:
            for row, col in king_moves:
                if 0 <= king_row + row < 8 and 0 <= king_col + col < 8:
                    if self.board[king_row + row][king_col + col] == 5:
                        return True
        elif self.board[king_row][king_col] == 5:
            for row, col in king_moves:
                if 0 <= king_row + row < 8 and 0 <= king_col + col < 8:
                    if self.board[king_row + row][king_col + col] == -5:
                        return True

        return False










