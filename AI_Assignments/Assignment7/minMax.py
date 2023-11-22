EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return -1
    elif is_winner(board, PLAYER_O):
        return 1
    elif is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = float('-inf')
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_O
        move_val = minimax(board, 0, False)
        board[i][j] = EMPTY
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

if __name__ == "__main__":
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Initial Board:")
    print_board(board)

    while True:
        # Player X move
        x, y = map(int, input("Enter your move (row and column, e.g., '1 2'): ").split())
        if board[x][y] == EMPTY:
            board[x][y] = PLAYER_X
        else:
            print("Invalid move, try again.")
            continue

        print_board(board)

        if is_winner(board, PLAYER_X):
            print("Player X wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # Player O move (AI)
        print("AI (Player O) is thinking...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_O

        print("AI's move:")
        print_board(board)

        if is_winner(board, PLAYER_O):
            print("Player O (AI) wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break