from random import randint

board = [
  ['-', '-', '-'],
  ['-', '-', '-'],
  ['-', '-', '-']
]
game_over = False

def generate_map(board):
    map = ""
    for i in board:
        for j in i:
            map += f"({j})"
        map += "\n"
    return map

def board_filled(board):
    for i in board:
        for j in i:
            if j == "-":
                return False
    return True

def ai_place(board, ai_piece):
    col = randint(0,2)
    row = randint(0,2)
    while board[row][col] != "-":
        col = randint(0,2)
        row = randint(0,2)
    board[row][col] = ai_piece

def won(board, test_piece):
    for row in range(3):
        complete_row = True
        for column in range(3):
            if board[row][column] != test_piece:
                complete_row = False
        if complete_row:
            return True
    
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != test_piece:
                complete_column = False
        if complete_column:
            return True
    
    # Test diagonals
    if board[0][0] == test_piece and board[1][1] == test_piece and board[2][2] == test_piece:
        return True
    if board[0][2] == test_piece and board[1][1] == test_piece and board[2][0] == test_piece:
        return True
    return False


piece = ""
while piece != "X" and piece != "O":
    choice = input("Enter X or O to pick a piece: ")
    if choice == "X" or choice == "O":
        piece = choice
    else:
        print("Not a valid piece. Try again.")

# AI piece
ai_piece = ""
if piece == "X":
    ai_piece = "O"
else:
    ai_piece = "X"

print(f"Map:\n{generate_map(board)}")
while not game_over:
    print("Place your piece down.")
    row_num = input("Enter a row number (1, 2, or 3): ")
    col_num = input("Enter a column number (1, 2, or 3): ")
    try:
        if board[int(row_num)-1][int(col_num)-1] != "-":
            print("There is already a piece there.")
            continue
        board[int(row_num)-1][int(col_num)-1] = piece
    except:
        print("Invalid entry. Both numbers have to be 1 through 3.")
        continue
    
    # Game ends if board is full
    if board_filled(board):
        print("Board is completely filled. Nobody wins! Sorry!")
        break
    
    # Check if you, main player, won
    if won(board, piece):
        print("Congratulations! You won the game!")
        break
    
    print("Your opponent is putting down their piece.")
    ai_place(board, ai_piece)
    
    # Test if opponent  won
    if won(board, ai_piece):
        print("Sorry, the AI bot beat you!")
        break
    print(f"Map:\n{generate_map(board)}")

print(f"Map:\n{generate_map(board)}")
