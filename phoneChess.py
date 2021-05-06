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
        """ Calculates possible moves that can be made for a given piece, and starting position, and returns a set of possiblities """
        availableSpaces = set()

        for move in self.calculateStraightSpaces(board, startingPos):
            availableSpaces.add(move)

        for move in self.calculateDiagonalSpaces(board, startingPos):
            availableSpaces.add(move)

        return availableSpaces

    def calculateValidNumbers(self, board, startingPos, currentPath="", validNumbers=None):
        """ Calculates valid phone numbers that can be made with the chess piece, with a given starting point, and returns a set """

        if validNumbers is None: # makes sure the validNumbers set is reset for the next call
            validNumbers = set()

        currentPath += board.getLocationValue(startingPos) # add the current position as the next character in the phone number
        for availableMove in self.calculateAvailableMoves(board, startingPos):
            if(len(currentPath) < 7):
                self.calculateValidNumbers(board, availableMove, currentPath, validNumbers)
            else: # if the current path is already 7 digits long, break out of the current loop, and add the number to the set
                validNumbers.add(currentPath)
                break
        
        return validNumbers

    def calculateAllValidNumbers(self, board, startingLocations):
        """ Calculates every possible valid phone number, from every valid starting point given, and returns the amount of valid numbers, and the sets of valid numbers """
        validNumberSets = [] # stores a list, of sets of valid numbers for each starting location
        for location in startingLocations:
            validNumberSets.append(self.calculateValidNumbers(board, location))

        validNumbersCount = 0
        for validNumberSet in validNumberSets:
            validNumbersCount += len(validNumberSet)
        
        return validNumbersCount, validNumberSets     


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

    def calculateValidNumbers(self, board, startingPos, currentPath="", validNumbers=set() ):
        """ Calculates valid phone numbers that can be made with the chess piece, with a given starting point, and returns a set """

        currentPath += board.getLocationValue(startingPos) # add the current position as the next character in the phone number
        for count, availableMove in enumerate(self.calculateAvailableMoves(board, startingPos)):
            if(count>0):
                self.madeFirstMove = True
            else:
                self.madeFirstMove = False

            if(len(currentPath) < 7):
                self.calculateValidNumbers(board, availableMove, currentPath, validNumbers)
            else: # if the current path is already 7 digits long, break out of the current loop, and add the number to the set
                validNumbers.add(currentPath)
                break
        
        return validNumbers
            

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
            return str(self.board[self.verticalSize-1-pos[1]][pos[0]])
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


# creates the different chess piece instances
king = King("King")
queen = Queen("Queen")
bishop = Bishop("Bishop")
rook = Rook("Rook")
knight = Knight("Knight")
pawn = Pawn("Pawn")


# sets up the chess board
phoneBoard = Board(3, 4)

phoneBoard.setRow(0, [1, 2, 3])
phoneBoard.setRow(1, [4, 5, 6])
phoneBoard.setRow(2, [7, 8, 9])
phoneBoard.setRow(3, ['*', 0, '#'])
phoneBoard.setInvalidSquare((0, 0)) # sets the '*' square as invalid
phoneBoard.setInvalidSquare((2, 0)) # sets the '#' square as invalid
print(phoneBoard)


if __name__ == '__main__': # if running this file directly
    validStartingLocations = [(1,3), (2,3), (0,2), (1,2), (2,2), (0,1), (0,2), (2,1)] # numbers 2-9 inclusive on the phone board, as starting locations to create phone numbers for

    print("Count of valid King numbers: ", king.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])
    print("Count of valid Queen numbers: ", queen.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])
    print("Count of valid Rook numbers: ", rook.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])
    print("Count of valid Bishop numbers: ", bishop.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])
    print("Count of valid Knight numbers: ", knight.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])
    print("Count of valid Pawn numbers: ", pawn.calculateAllValidNumbers(phoneBoard, validStartingLocations)[0])