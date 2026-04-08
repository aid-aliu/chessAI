from board import Board

def clear_board(board):
    board.board = [[0 for _ in range(8)] for _ in range(8)]

def run_scenario(title, pieces, white_turn):
    board = Board()
    clear_board(board)

    for row, col, piece in pieces:
        board.board[row][col] = piece

    board.white_turn = white_turn

    print(f"\n===== {title} =====")
    board.print_board()
    print("white_turn:", board.white_turn)
    print("check:", board.check())
    print("checkmate:", board.checkmate())
    print("stalemate:", board.stalemate())


# 1) Checkmate
# Black king a8, White queen b7, White king c6
# Black to move
run_scenario(
    "SCENARIO 1 - CHECKMATE",
    [
        (0, 0, -5),
        (1, 1, 6),
        (2, 2, 5),
    ],
    False
)

# expected:
# check: True
# checkmate: True
# stalemate: False


# 2) Stalemate
# Black king a8, White queen c7, White king c6
# Black to move
run_scenario(
    "SCENARIO 2 - STALEMATE",
    [
        (0, 0, -5),
        (1, 2, 6),
        (2, 2, 5),
    ],
    False
)

# expected:
# check: False
# checkmate: False
# stalemate: True


# 3) Mirror checkmate
# Black king h8, White queen g7, White king f6
# Black to move
run_scenario(
    "SCENARIO 3 - MIRROR CHECKMATE",
    [
        (0, 7, -5),
        (1, 6, 6),
        (2, 5, 5),
    ],
    False
)

# expected:
# check: True
# checkmate: True
# stalemate: False


# 4) Mirror stalemate
# Black king h8, White queen f7, White king f6
# Black to move
run_scenario(
    "SCENARIO 4 - MIRROR STALEMATE",
    [
        (0, 7, -5),
        (1, 5, 6),
        (2, 5, 5),
    ],
    False
)

# expected:
# check: False
# checkmate: False
# stalemate: True


# 5) Control position: not mate, not stalemate
# Black king a8, White king c6
# Black to move
run_scenario(
    "SCENARIO 5 - NORMAL CONTROL",
    [
        (0, 0, -5),
        (2, 2, 5),
    ],
    False
)

# expected:
# check: False
# checkmate: False
# stalemate: False