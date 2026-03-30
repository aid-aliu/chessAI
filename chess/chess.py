from board import Board

# 0 empty, 1 pawn, 2 rook, 3 knight, 4 bishop, 5 king, 6 queen
# white = positive, black = negative

print("===== TEST 1: INITIAL BOARD =====")
board = Board()
board.print_board()
print("Expected: normal starting position")
print("Expected white_turn: True")
print("Actual white_turn:", board.white_turn)


print("\n===== TEST 2: SIMPLE LEGAL MOVE =====")
board = Board()
print("Move white pawn e2 -> e4 : try_move(6,4,4,4)")
print("Result:", board.try_move(6, 4, 4, 4))
print("Expected: True")
board.print_board()
print("Expected: board[6][4] = 0, board[4][4] = 1")
print("Expected white_turn: False")
print("Actual white_turn:", board.white_turn)


print("\n===== TEST 3: OUT OF TURN MOVE =====")
board = Board()
print("Black tries to move first: e7 -> e5 : try_move(1,4,3,4)")
print("Result:", board.try_move(1, 4, 3, 4))
print("Expected: False")
board.print_board()


print("\n===== TEST 4: PINNED PIECE SHOULD NOT BE ALLOWED TO MOVE =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[6][4] = 2      # white rook e2
board.board[0][4] = -2     # black rook e8

print("Before move:")
board.print_board()
print("White rook e2 -> f2 : try_move(6,4,6,5)")
print("Result:", board.try_move(6, 4, 6, 5))
print("Expected: False, because rook was shielding the king")
print("Board should stay unchanged:")
board.print_board()


print("\n===== TEST 5: KING MOVES INTO ROOK ATTACK =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8

print("Before move:")
board.print_board()
print("White king e1 -> e2 : try_move(7,4,6,4)")
print("Result:", board.try_move(7, 4, 6, 4))
print("Expected: False, because e2 is attacked by the rook")
print("Board should stay unchanged:")
board.print_board()


print("\n===== TEST 6: SIDE IN CHECK CAN BLOCK THE CHECK =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8
board.board[6][3] = 6      # white queen d2

print("Before move:")
board.print_board()
print("White queen d2 -> e2 : try_move(6,3,6,4)")
print("Result:", board.try_move(6, 3, 6, 4))
print("Expected: True, because queen blocks the rook line")
print("After move:")
board.print_board()
print("Expected white_turn: False")
print("Actual white_turn:", board.white_turn)


print("\n===== TEST 7: SIDE IN CHECK CANNOT IGNORE THE CHECK =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8
board.board[7][6] = 3      # white knight g1

print("Before move:")
board.print_board()
print("White knight g1 -> f3 : try_move(7,6,5,5)")
print("Result:", board.try_move(7, 6, 5, 5))
print("Expected: False, because white is in check and this move does not solve it")
print("Board should stay unchanged:")
board.print_board()


print("\n===== TEST 8: KING CANNOT MOVE NEXT TO ENEMY KING =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[5][4] = -5     # black king e3

print("Before move:")
board.print_board()
print("White king e1 -> e2 : try_move(7,4,6,4)")
print("Result:", board.try_move(7, 4, 6, 4))
print("Expected: False, because kings would become adjacent")
print("Board should stay unchanged:")
board.print_board()


print("\n===== TEST 9: KING MAKES A LEGAL ESCAPE MOVE =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8

print("Before move:")
board.print_board()
print("White king e1 -> f1 : try_move(7,4,7,5)")
print("Result:", board.try_move(7, 4, 7, 5))
print("Expected: True, because f1 is not on the rook file")
print("After move:")
board.print_board()
print("Expected white_turn: False")
print("Actual white_turn:", board.white_turn)


print("\n===== TEST 10: SAME SELF-CHECK LOGIC FOR BLACK SIDE =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = False

board.board[0][4] = -5     # black king e8
board.board[1][4] = -2     # black rook e7
board.board[7][4] = 2      # white rook e1

print("Before move:")
board.print_board()
print("Black rook e7 -> f7 : try_move(1,4,1,5)")
print("Result:", board.try_move(1, 4, 1, 5))
print("Expected: False, because black rook was shielding black king")
print("Board should stay unchanged:")
board.print_board()


print("\n===== TEST 11: DIRECT CHECK() TRUE TEST =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8

board.print_board()
print("check() result:", board.check())
print("Expected: True")


print("\n===== TEST 12: DIRECT CHECK() FALSE TEST =====")
board = Board()
board.board = [[0 for _ in range(8)] for _ in range(8)]
board.white_turn = True

board.board[7][4] = 5      # white king e1
board.board[0][4] = -2     # black rook e8
board.board[5][4] = 6      # white queen e3 blocks the rook line

board.print_board()
print("check() result:", board.check())
print("Expected: False")