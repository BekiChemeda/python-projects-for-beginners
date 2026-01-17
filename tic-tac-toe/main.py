import random

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentPlayer = "X"
winner = None
gameRunning = True

## printing the 3x3 game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

## take player input
def playerInput(board):
    notValid = True
    while notValid:
        inp = int(input("Select a spot 1-9: "))
        if inp >= 1 and inp <= 9:
            if board[inp-1] == "_":
                board[inp-1] = currentPlayer
                notValid=False
            else:
                print("Spot already taken!")
        else:
            print("Please enter a valid number between 1 and 9.")

# Check for win or tie

# Check rows
def checkRows(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "_":
            winner = board[i]
            return True

    # Check Columns
def CheckCol(board):
    global winner
    for i in range(0,3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "_":
            winner = board[i]
            return True
    # Check Diagonal 
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board [0] != "_":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

def checkWin():
    if checkRows(board) or CheckCol(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        global gameRunning
        gameRunning = False

## Check Tie 
def CheckTie(board):
    global gameRunning
    if "_" not in board:
        printBoard(board)
        print("It's a Tie!")
        gameRunning = False

        
## Switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    CheckTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    CheckTie(board)
    