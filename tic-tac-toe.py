class TicTacToe:
    board = [['-']*3 for _ in range(3)]
    spacesLeft = 9
    def printBoard(self):
        for row in self.board:
            print('|'.join(row))
    def addMove(self,x,y,token):
        if self.board[x][y] == '-':
            self.board[x][y] = token
            self.spacesLeft -= 1
            return True
        return False
    def isBoardFull(self):
        return self.spacesLeft == 0
    def makeAIMove(self):
        for rowIdx in range(3):
            for idx in range(3):
                if self.board[rowIdx][idx] == '-':
                    self.addMove(rowIdx,idx,'O')
                    return True
        raise Exception('No valid moves left for the AI') 
    def hasWon(self, x, y, token):
        won = True
        #check row
        for i in range(3):
            if self.board[x][i] != token:
                won = False
        # check column
        for i in range(3):
            if self.board[i][y] != token:
                won  = False
    def play(self):
        self.printBoard()
        while not self.isBoardFull():
            userX = input('Please enter a row value: ')
            userY = input('Please enter a column value: ')
            try:
                userX = int(userX)
                userY = int(userY)
            except ValueError:
                print('Input must be a number')
                continue
            if userX < 0 or userX > 2 or userY < 0 or userY > 2:
                print('Row and column must be within the range 0-2')
                continue
            worked = self.addMove(userX,userY,'X')
            if not worked:
                print('Space already taken, try again')
                continue
            if not self.isBoardFull():
                self.makeAIMove()
            self.printBoard()



s = TicTacToe()
s.play()
