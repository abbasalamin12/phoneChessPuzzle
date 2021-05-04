from math import inf as inf

class ChessPiece:
    def __init__(self, name):
        self.name = name
        self.moveRange = 0

    def calculateStraightSpaces(self, board, startingPos):
        """ Returns a set of available spaces that a piece can move to straightly. This includes spaces that are directly up/down/left/right """
        if(not board.isSquareValid(startingPos)):
            raise IndexError("The coordinates must be in range")

        availableSpaces = set()

        xPos = startingPos[0]
        yPos = startingPos[1]

        xRange = board.getRange(self.moveRange, xPos, "horizontal")
        yRange = board.getRange(self.moveRange, yPos, "vertical")

        for potentialXCoord in xRange:
            if(potentialXCoord != xPos):
                if(board.isSquareValid( (potentialXCoord, yPos) )): # if the new square is valid, add it to the available spaces
                    availableSpaces.add( (potentialXCoord, yPos) )

        for potentialYCoord in yRange:
            if(potentialYCoord != yPos):
                if(board.isSquareValid( (xPos, potentialYCoord) )): # if the new square is valid, add it to the available spaces
                    availableSpaces.add( (xPos, potentialYCoord) )

        return availableSpaces

    def calculateDiagonalSpaces(self, board, startingPos):
        """ Returns a set of available spaces that a piece can move to diagonally. This includes spaces that are north-east, north-west, south-east, and south-west """
        availableSpaces = set()

        if(not board.isSquareValid(startingPos)):
            raise IndexError("The coordinates must be in range")

        xPos = startingPos[0]
        yPos = startingPos[1]

        xRange = board.getRange(self.moveRange, xPos, "horizontal")
        xMax = max(xRange)
        xMin = min(xRange)
        
        yRange = board.getRange(self.moveRange, yPos, "vertical")
        yMax = max(yRange)
        yMin = min(yRange)

        # north-east squares (add 1 to x and y)
        for count, potentialXCoord in enumerate(range(xPos+1, xMax+1)):            
            if(yPos+count+1 <= yMax):
                if(board.isSquareValid((potentialXCoord, yPos+count+1))):
                    availableSpaces.add((potentialXCoord, yPos+count+1))

        # # south-west squares (subtract 1 from x and y)
        for count, potentialXCoord in enumerate(range(xPos-1, xMin-1, -1)):
            if(yPos-count-1 >= yMin):
                if(board.isSquareValid((potentialXCoord, yPos-count-1))):
                    availableSpaces.add((potentialXCoord, yPos-count-1))

        # # north-west squares (subtract 1 from x and add 1 to y)
        for count, potentialXCoord in enumerate(range(xPos-1, xMin-1, -1)):
            if(yPos+count+1 <= yMax):
                if(board.isSquareValid((potentialXCoord, yPos+count+1))):
                    availableSpaces.add((potentialXCoord, yPos+count+1))

        # south-east squares (add 1 to x and subtract 1 to y)
        for count, potentialXCoord in enumerate(range(xPos+1, xMax+1)):
            if(yPos-count-1 >= yMin):
                if(board.isSquareValid((potentialXCoord, yPos-count-1))):
                    availableSpaces.add((potentialXCoord, yPos-count-1))

        return availableSpaces

    def calculateAvailableMoves(self, board, startingPos):
        availableSpaces = set()

        for move in self.calculateStraightSpaces(board, startingPos):
            availableSpaces.add(move)

        for move in self.calculateDiagonalSpaces(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces

class King(ChessPiece):
    def __init__(self, name):
        super().__init__("King")
        self.moveRange = 1

class Queen(ChessPiece):
    def __init__(self, name):
        super().__init__("Queen")
        self.moveRange = inf

class Rook(ChessPiece):
    def __init__(self, name):
        super().__init__("Rook")
        self.moveRange = inf

    def calculateAvailableMoves(self, board, startingPos):
        availableSpaces = set()

        for move in self.calculateStraightSpaces(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces

class Bishop(ChessPiece):
    def __init__(self, name):
        super().__init__("Bishop")
        self.moveRange = inf

    def calculateAvailableMoves(self, board, startingPos):
        availableSpaces = set()

        for move in self.calculateDiagonalSpaces(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces

class Knight(ChessPiece):
    def __init__(self, name):
        super().__init__("Knight")
        self.moveRange = 2
        self.secondMoveRange = 1

    def calculateLShapeSpaces(self, board, startingPos):
        """ Returns a set of available spaces that a piece can move to using L shapes """        
        if(not board.isSquareValid(startingPos)):
            raise IndexError("The coordinates must be in range")
            
        availableSpaces = set()

        xPos = startingPos[0]
        yPos = startingPos[1]

        potentialCoordinates = []      

        potentialCoordinates.append((xPos+self.moveRange, yPos+self.secondMoveRange)) # right, down
        potentialCoordinates.append((xPos+self.moveRange, yPos-self.secondMoveRange)) # right, up
        potentialCoordinates.append((xPos-self.moveRange, yPos+self.secondMoveRange)) # left, down
        potentialCoordinates.append((xPos-self.moveRange, yPos-self.secondMoveRange)) # left, up
        potentialCoordinates.append((xPos+self.secondMoveRange, yPos+self.moveRange)) # up, right
        potentialCoordinates.append((xPos-self.secondMoveRange, yPos+self.moveRange)) # up, left
        potentialCoordinates.append((xPos+self.secondMoveRange, yPos-self.moveRange)) # down, right
        potentialCoordinates.append((xPos-self.secondMoveRange, yPos-self.moveRange)) # down, left

        for potentialCoordinate in potentialCoordinates:
            if(board.isSquareValid(potentialCoordinate)):
                availableSpaces.add(potentialCoordinate)

        return availableSpaces

    def calculateAvailableMoves(self, board, startingPos):
        availableSpaces = set()

        for move in self.calculateLShapeSpaces(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces

class Pawn(ChessPiece):
    def __init__(self, name):
        super().__init__("Pawn")
        self.madeFirstMove = False
        self.moveRange = 2
        self.secondMoveRange = 1

    def calculatePawnMoves(self, board, startingPos):
        if(not board.isSquareValid(startingPos)):
            raise IndexError("The coordinates must be in range")

        availableSpaces = set()

        xPos = startingPos[0]
        yPos = startingPos[1]

        if(board.isSquareValid((xPos, yPos+1))):
            availableSpaces.add((xPos, yPos+1))
        if(self.madeFirstMove == False):
            if(board.isSquareValid((xPos, yPos+2))):
                availableSpaces.add((xPos, yPos+2))
        
        return availableSpaces
        
    def calculateAvailableMoves(self, board, startingPos):
        availableSpaces = set()

        for move in self.calculatePawnMoves(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces
            

    

class Board:
    def __init__(self, horizontalSize, verticalSize):
        """ Initialises a board object with a default 2d array """
        self.horizontalSize = horizontalSize
        self.verticalSize = verticalSize
        self.board = [[x for x in range(horizontalSize)] for y in range(verticalSize)] # creates a 2d array to represent the board

        self.invalidSquares = set()
    
    def setRow(self, selectedRow, newRow):
        """ Used to set a row to a custom value, for when the default is not appropriate """
        if(selectedRow>=0 and selectedRow<self.verticalSize):
            self.board[selectedRow] = newRow

    def setInvalidSquare(self, pos):
        """ This marks a square on the board as invalid, so no pieces can go on it """
        if(pos[0] < self.horizontalSize and pos[0] >= 0  and pos[1] < self.verticalSize and pos[1] >= 0): # if the square is within range, add it to the list
            self.invalidSquares.add(pos)
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
        if(pos in self.invalidSquares): # if the square has been manually marked as invalid
            return False
        elif( not (pos[0] < self.horizontalSize and pos[0] >= 0  and pos[1] < self.verticalSize and pos[1] >= 0)): # if the square is out of range
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
                if(currentPos+movementRange >= self.verticalSize):
                    rangeMax = self.verticalSize
                else:
                    rangeMax = currentPos+movementRange+1
            elif(direction=="horizontal"):
                if(currentPos+movementRange >= self.horizontalSize):
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

    
king = King("King")
queen = Queen("Queen")
bishop = Bishop("Bishop")
rook = Rook("Rook")
knight = Knight("Knight")
pawn = Pawn("Pawn")


phoneBoard = Board(3, 4)

phoneBoard.setRow(0, [1, 2, 3])
phoneBoard.setRow(1, [4, 5, 6])
phoneBoard.setRow(2, [7, 8, 9])
phoneBoard.setRow(3, ['*', 0, '#'])
phoneBoard.setInvalidSquare((0, 0)) # sets the '*' square as invalid
phoneBoard.setInvalidSquare((2, 0)) # sets the '#' square as invalid
print(phoneBoard)


print("Available King moves from 5 square: ")
print(king.calculateAvailableMoves(phoneBoard, (1,2)))

print("Available Queen moves from 3 square: ")
print(queen.calculateAvailableMoves(phoneBoard, (2,3)))

print("Available Bishop moves from 3 square: ")
print(bishop.calculateAvailableMoves(phoneBoard, (2,3)))

print("Available Rook moves from 3 square: ")
print(rook.calculateAvailableMoves(phoneBoard, (2,3)))

print("Available Knight moves from 3 square: ")
print(knight.calculateAvailableMoves(phoneBoard, (0,1)))

print("Available Pawn moves from 0 square: ")
print(pawn.calculateAvailableMoves(phoneBoard, (1,0)))