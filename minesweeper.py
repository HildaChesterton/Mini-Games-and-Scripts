import random

def create_board(rows, columns, mines):
    board = [[' ' for i in range(columns)] for j in range(rows)]
    for i in range(mines):
        row, col = random.randint(0, rows - 1), random.randint(0, columns - 1)
        while board[row][col] == '*':
            row, col = random.randint(0, rows - 1), random.randint(0, columns - 1)
        board[row][col] = '*'
    return board

def print_board(board):
    print('  | ' + ' | '.join([str(i) for i in range(len(board[0]))]))
    print('--|-' + '-|-'.join(['-' for i in range(len(board[0]))]))
    for i in range(len(board)):
        print(str(i) + ' | ' + ' | '.join(board[i]))
        print('--|-' + '-|-'.join(['-' for i in range(len(board[0]))]))

def count_mines(row, col, board):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if row + i >= len(board) or row + i < 0 or col + j >= len(board[0]) or col + j < 0:
                continue
            if board[row + i][col + j] == '*':
                count += 1
    return count

def play_game():
    rows, columns, mines = 8, 8, 10
    board = create_board(rows, columns, mines)
    revealed = [[' ' for i in range(columns)] for j in range(rows)]

    while True:
        print_board(revealed)
        row, col = input("Enter row and column (e.g. 2,3): ").split(',')
        row, col = int(row), int(col)
        if board[row][col] == '*':
            print_board(board)
            print("Game over! You hit a mine.")
            break
        elif revealed[row][col] != ' ':
            print("That square has already been revealed.")
        else:
            count = count_mines(row, col, board)
            revealed[row][col] = str(count) if count > 0 else '-'
            if sum([row.count(' ') for row in revealed]) == mines:
                print_board(board)
                print("Congratulations, you won!")
                break

def main():
    play_game()

if __name__ == "__main__":
    main()
