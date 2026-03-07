from board import Board

board = Board()
board.print_board()

# 0 empty, 1 pawn, 2 rook, 3 knight, 4 bishop, 5 king, 6 queen


print("=============================================")
board.move_piece(6, 0, 5, 0)
board.print_board()

print("=============================================")
board.move_piece(1, 0, 2, 0)
board.print_board()

