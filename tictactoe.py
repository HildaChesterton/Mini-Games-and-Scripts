def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('-------------')

def get_move(player, board):
    while True:
        move = input("Player " + player + ", enter your move (row, column): ")
        row, col = move.split(',')
        row, col = int(row), int(col)
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Row and column must be between 0 and 2.")
        elif board[row][col] != ' ':
            print("Invalid move. That square is already occupied.")
        else:
            return row, col

def check_win(player, board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def play_game():
    board = [[' ' for i in range(3)] for j in range(3)]
    players = ['X', 'O']
    turn = 0
    while True:
        print_board(board)
        row, col = get_move(players[turn], board)
        board[row][col] = players[turn]
        if check_win(players[turn], board):
            print_board(board)
            print("Player " + players[turn] + " wins!")
            break
        if all([board[i][j] != ' ' for i in range(3) for j in range(3)]):
            print_board(board)
            print("Tie game.")
            break
        turn = 1 - turn

def main():
    play_game()

if __name__ == "__main__":
    main()
