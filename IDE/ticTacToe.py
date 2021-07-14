#A tictactoe game with AI
class tictactoe:
    def __init__(self):
        self.board=[' ' for x in range(10)]

    def insertLetter(self,letter,pos):
        self.board[pos]=letter

    def spaceIsFree(self,pos):
        return self.board[pos]==' '

    def printBoard(self):
        print("   |   |")
        print(' '+self.board[1]+" | "+self.board[2]+" | "+self.board[3])
        print("   |   |")
        print("----------")
        print("   |   |")
        print(' '+self.board[4]+" | "+self.board[5]+" | "+self.board[6])
        print("   |   |")
        print("----------")
        print("   |   |")
        print(' '+self.board[7]+" | "+self.board[8]+" | "+self.board[9])
        print("   |   |")

    def isWinner(self,bo,le):
        return ((bo[1]==le and bo[2]==le and bo[3]==le) or
        (bo[4]==le and bo[5]==le and bo[6]==le) or
        (bo[7]==le and bo[8]==le and bo[9]==le) or
        (bo[1]==le and bo[4]==le and bo[7]==le) or
        (bo[2]==le and bo[5]==le and bo[8]==le) or
        (bo[3]==le and bo[6]==le and bo[9]==le) or
        (bo[1]==le and bo[5]==le and bo[9]==le) or
        (bo[3]==le and bo[5]==le and bo[7]==le))

    def playerMove(self):
        run=True

        while (run):
            move=int(input
            ("Please select a position to place \'X\' from 1 to 9: "))

            if(move>0 and move<10):
                if(self.spaceIsFree(move)):
                    run=False
                    self.insertLetter('X',move)
                else:
                    print("This position is taken!")
            else:
                print("Choose a valid option!")

    def compMove(self):
        possibleMoves=[x for x, letter in enumerate(self.board)
        if letter==' ' and x!=0]
        move=0

        for let in ['O','X']:
            for i in possibleMoves:
                boardCopy=self.board[:]
                boardCopy[i]=let

                if self.isWinner(boardCopy,let):
                    move=i
                    return move

        cornersOpen=[]
        for i in possibleMoves:
            if i in[1,3,7,9]:
                cornersOpen.append(i)

        if len(cornersOpen) > 0:
            move=self.selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move=5
            return move

        edgesOpen=[]
        for i in possibleMoves:
            if i in[2,4,6,8]:
                edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move=self.selectRandom(edgesOpen)
            return move

        return move

    def selectRandom(self,li):
        import random
        ln=len(li)
        r=random.randrange(0,ln)
        return li[r]

    def isBoardFull(self,board):
        if self.board.count(' ')>1:
            return False
        else:
            return True

    def main(self):
        print("Welcome to Tic Tac Toe")
        self.printBoard(self.board)

        while not(self.isBoardFull(self.board)):
            if not(self.isWinner(self.board,'O')):
                self.playerMove()
                self.printBoard(self.board)
            else:
                print("O\'s won the game!")
                break

            if not(self.isWinner(self.board,'X')):
                move=self.compMove()

                if(move==0 or self.isBoardFull(self.board)):
                    print("Tie Game!")
                else:
                    self.insertLetter('O',move)
                    print("Computer placed an \'O\' in position",move)
                    self.printBoard(self.board)

            else:
                print("X\'s won the game!")
                break

if __name__=='__main__':
    game=tictactoe()
    game.main()
