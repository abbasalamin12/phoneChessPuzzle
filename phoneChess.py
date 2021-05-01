from math import inf as inf

class ChessPiece:
    def __init__(self, name, firstMoveRange, secondMoveRange, canMoveDiagonally, canMoveStraight, canOnlyMoveUp=False):
        """ Initialises a chess piece object that has its own movement rules """
        self.name = name
        self.firstMoveRange = firstMoveRange # every piece gets a first move
        self.secondMoveRange = secondMoveRange # this is only relavant for the knight piece, which moves 2 spaces in one direction, then 1 space in another direction
        self.canMoveDiagonally = canMoveDiagonally
        self.canMoveStraight = canMoveStraight
        self.canOnlyMoveUp = canOnlyMoveUp # this is relevant for pawn pieces which can only move upwards

    def calculateStraightSpaces(self, board, startingPos):
        availableSpaces = set()

        xPos = startingPos[0]
        yPos = startingPos[1]

        for potentialXCoord in board.getRange(self.firstMoveRange, xPos, "horizontal"):
            if(potentialXCoord != xPos):
                if(board.isSquareValid( (potentialXCoord, yPos) )): # if the new square is valid, add it to the available spaces
                    availableSpaces.add( (potentialXCoord, yPos) )

        for potentialYCoord in board.getRange(self.firstMoveRange, yPos, "vertical"):
            if(potentialYCoord != yPos):
                if(board.isSquareValid( (xPos, potentialYCoord) )): # if the new square is valid, add it to the available spaces
                    availableSpaces.add( (xPos, potentialYCoord) )

        return availableSpaces


    def calculateDiagonalSpaces(self, board, startingPos):
        #TODO
        availableSpaces = set()

    def calculateAvailableMoves(self, board, startingPos):
        #TODO
        availableSpaces = set()


class Board:
    def __init__(self, horizontalSize, verticalSize):
        """ Initialises a board object with a default 2d array """
        self.horizontalSize = horizontalSize
        self.verticalSize = verticalSize
        self.board = [[x for x in range(horizontalSize)] for y in range(verticalSize)] # creates a 2d array to represent the board

        self.invalidSquares = []
    
    def setRow(self, selectedRow, newRow):
        """ Used to set a row to a custom value, for when the default is not appropriate """
        if(selectedRow>=0 and selectedRow<=self.verticalSize-1):
            self.board[selectedRow] = newRow

    def setInvalidSquare(self, pos):
        """ This marks a square on the board as invalid, so no pieces can go on it """
        if(pos[0] < self.horizontalSize and pos[0] >= 0  and pos[1] < self.verticalSize and pos[1] >= 0):
            self.invalidSquares.append(pos)
        else:
            raise IndexError("The coordinates must be in range")

    def getInvalidSquareValues(self):
        """ This returns a list with all of the values at invalid square coordinates """
        invalidSquareValues = []
        for invalidSquare in self.invalidSquares:
            invalidSquareValues.append(self.getLocationValue(invalidSquare))
        return invalidSquareValues

    def isSquareValid(self, pos):
        """ Returns true if the given coordinates are for a valid square, otherwise it returns false """
        if(pos in self.invalidSquares):
            return False
        else:
            return True
    
    def getRange(self, movementRange, currentPos, direction):
        """ Returns a movement range taking the board's boundaries, and the piece's movement into consideration """
        if(movementRange == inf):
            if(direction=="vertical"):
                return range(0, self.verticalSize)
            if(direction=="horizontal"):
                return range(0, self.horizontalSize)
        else:
            if(direction=="vertical"):
                if(currentPos+movementRange > self.verticalSize):
                    rangeMax = self.verticalSize
                else:
                    rangeMax = currentPos+movementRange+1
            elif(direction=="horizontal"):
                if(currentPos+movementRange > self.horizontalSize):
                    rangeMax = self.horizontalSize
                else:
                    rangeMax = currentPos+movementRange+1

            if(currentPos-movementRange < 0):
                rangeMin = 0
            else:
                rangeMin = currentPos-movementRange

            return range(rangeMin, rangeMax)
        


    def getLocationValue(self, pos):
        """ Takes a tuple that represents coordinates and returns whats on those coordinates """
        if(pos[0] < self.horizontalSize and pos[0] >= 0  and pos[1] < self.verticalSize and pos[1] >= 0):
            return self.board[self.verticalSize-1-pos[1]][pos[0]]
        else:
            raise IndexError("The coordinates must be in range")

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
phoneBoard.setInvalidSquare((0, 0)) # sets the '*' square as invalid
phoneBoard.setInvalidSquare((2, 0)) # sets the '#' square as invalid
print(phoneBoard)

# print(phoneBoard.getInvalidSquareValues())
# print(phoneBoard.getLocationValue((0, 1)))

print(king.calculateStraightSpaces(phoneBoard, (0,0)))