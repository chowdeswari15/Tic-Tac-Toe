board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-----')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return ' ' not in board
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[human_move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI has made its move:")
        print_board()

        if check_winner(board, 'O'):
            print("AI wins, You Lost better luck next time!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
play_game()
