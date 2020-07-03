class Board:
    def __init__(self):
        self.board =  [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    # check whether or not space is occupied by 'X' or' 'O'
    # 1 <= pos <= 9
    def isFree(self, pos: int):
        row = (pos - 1) // 3 
        col = pos % 3 - 1
        return self.board[row][col] == ' '

    # 1 <= pos <= 9
    def updateBoard(self, pos:int, symbol : str):
        row = (pos - 1) // 3
        col = pos % 3 - 1
        self.board[row][col] = symbol
    
    def clearBoard(self):
        self.board =  [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    def drawBoard(self):
        print(f' {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ')
        print('-----------')
        print(f' {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ')
        print('-----------')
        print(f' {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ')

    @staticmethod   
    def drawSampleBoard():
        print(' 1 | 2 | 3 ')
        print('-----------')
        print(' 4 | 5 | 6 ')
        print('-----------')
        print(' 7 | 8 | 9 ')

    # return 'X' if player 1 has won the game
    #        'O' if player 2 has won the game
    #        'N' if there is no winner
    def checkWinner(self):
        # check rows and columns
        for i in range(3):
            # rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            # columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[2][0]

        return 'N'

    # check if there is any space left to place 'X' or 'O'
    def isBoardFUll(self):
        for i in range(3):
            if ' ' in self.board[i]:
                return False   
        return True
            
        




           

