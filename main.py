from board import Board
myBoard = Board()

def playerMove(player: int):
    validMove = False
    while not validMove:
        move = input(f"Player {player}: Please select your move: ")     
        try:
            move = int(move)
            if move > 0 and move < 10 and myBoard.isFree(move):
                validMove = True 
                if player == 1:
                    myBoard.updateBoard(move,'X') 
                else:
                     myBoard.updateBoard(move,'O')
            else:
                print("Invalid Move")
        except:
            print("Please enter an integer between 1 to 9")

          
print("Welcome to 2 player Tic Tac Toe")
print("Please enter number 1 to 9 to indicate your move")
Board.drawSampleBoard()

# game loop
run = True
currentPlayer = 1
while run:
    
    winner = myBoard.checkWinner()
    if winner == 'X':
        print("Player 1 won the game !")
        run = False
    elif winner == 'O':
        print("Player 2 won the game !")
        run = False
    elif myBoard.isBoardFUll():
        print('Tie game!')
        run = False 
    else:
        playerMove(currentPlayer)
        myBoard.drawBoard()
        if currentPlayer == 1:
            currentPlayer = 2
        else:
            currentPlayer = 1