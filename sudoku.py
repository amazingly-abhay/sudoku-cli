import random

def generate_board(difficulty='easy'):
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if difficulty == 'medium':
        for _ in range(20):
            x, y = random.randint(0, 8), random.randint(0, 8)
            board[x][y] = 0
    elif difficulty == 'hard':
        for _ in range(30):
            x, y = random.randint(0, 8), random.randint(0, 8)
            board[x][y] = 0
    return board


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(f"{board[i][j]} ", end="")


def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True


def is_solved(board):
    for row in board:
        if 0 in row:
            return False
    return True


def play_sudoku():
    print("Welcome to CLI Sudoku!")
    
    valid_difficulties = ['easy', 'medium', 'hard']
    difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    
    while difficulty not in valid_difficulties:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Select difficulty (easy, medium, hard): ").lower()
    
    board = generate_board(difficulty)
    
    while not is_solved(board):
        print_board(board)
        user_input = input("Enter row, column, and number (e.g., 1 2 3) or 'q' to quit: ").lower()
        
        if user_input == 'q':
            print("Exiting the game. Goodbye!")
            break
        
        try:
            row, col, num = map(int, user_input.split())
            if is_valid_move(board, row - 1, col - 1, num):
                board[row - 1][col - 1] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers in the format: row column number.")
    
    if is_solved(board):
        print("Congratulations! You solved the Sudoku.")
        print_board(board)



if __name__ == "__main__":
    play_sudoku()

