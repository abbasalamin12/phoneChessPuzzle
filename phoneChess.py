from math import inf as inf

class ChessPiece:
    def __init__(self, name, firstMoveRange, secondMoveRange, canMoveDiagonally, canMoveStraight):
        """ Initialises a chess piece object that has its own movement rules """
        self.name = name
        self.firstMoveRange = firstMoveRange # every piece gets a first move
        self.secondMoveRange = secondMoveRange # this is only relavant for the knight piece, which moves 2 spaces in one direction, then 1 space in another direction
        self.canMoveDiagonally = canMoveDiagonally
        self.canMoveStraight = canMoveStraight

    def calculateStraightSpaces(self, board, startingPos):
        #TODO
        availableSpaces = []

    def calculateDiagonalSpaces(self, board, startingPos):
        #TODO
        availableSpaces = []

    def calculateAvailableMoves(self, board, startingPos):
        #TODO
        availableMoves = []


class Board:
    def __init__(self, horizontalSize, verticalSize):
        """ Initialises a board object with a default 2d array """
        self.horizontalSize = horizontalSize
        self.verticalSize = verticalSize
        self.board = [[x for x in range(horizontalSize)] for y in range(verticalSize)] # creates a 2d array to represent the board
    
    def setRow(self, selectedRow, newRow):
        """ Used to set a row to a custom value, for when the default is not appropriate """
        if(selectedRow>=0 and selectedRow<=self.verticalSize-1):
            self.board[selectedRow] = newRow

    def __str__(self):
        """ Returns a printable version of the board that is easier to visualise. """
        viewableBoard = ""
        for y in self.board:
            for x in y:
                viewableBoard += str(x) +"    "
            viewableBoard += "\n"
        return viewableBoard

    
king = ChessPiece("King", 1, 0, True, True)
queen = ChessPiece("Queen", inf, 0, True, True)
bishop = ChessPiece("Bishop", inf, 0, True, False)
rook = ChessPiece("Rook", inf, 0, False, True)
knight = ChessPiece("Knight", 2, 1, False, True)


phoneBoard = Board(3, 4)

phoneBoard.setRow(0, [1, 2, 3])
phoneBoard.setRow(1, [4, 5, 6])
phoneBoard.setRow(2, [7, 8, 9])
phoneBoard.setRow(3, ['*', 0, '#'])
print(phoneBoard)