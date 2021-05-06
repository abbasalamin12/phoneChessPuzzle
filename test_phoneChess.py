import unittest
import phoneChess
from math import inf

class TestPhoneChess(unittest.TestCase):

    def test_calculateAvailableMoves_King(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for king chess piece

        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (0,3)), {(0,2), (1,2), (1,3)}) # from the 1 position, the king should be able to move to the 4, 5, and 2 positions
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (1,3)), {(0,2), (1,2), (0,3), (2,2), (2,3)}) # from the 2 position, the king should be able to move to the 1, 4, 5, 6, and 3 positions
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (2,3)), {(1,3), (1,2), (2,2)}) # testing from 3 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (0,2)), {(0,3), (0,1), (1,3), (1,2), (1,1)}) # testing from 4 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (1,2)), {(0,3), (0,2), (0,1), (1,3), (1,1), (2,3), (2,2), (2,1)}) # testing from 5 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (2,2)), {(2,3), (2,1), (1,3), (1,2), (1,1)}) # testing from 6 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (0,1)), {(0,2), (1,2), (1,1), (1,0)}) # testing from 7 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (1,1)), {(0,1), (0,2), (1,2), (1,0), (2,2), (2,1)}) # testing from 8 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (2,1)), {(2,2), (1,0), (1,1), (1,2)}) # testing from 9 position 
        self.assertEqual(phoneChess.king.calculateAvailableMoves(board, (1,0)), {(0,1), (1,1), (2,1)}) # testing from 0 position

    def test_calculateAvailableMoves_Queen(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for queen chess piece

        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (0,3)), {(0,2), (1,2), (1,3), (2,3), (0,1), (2,1)}) # testing from 1 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (1,3)), {(0,2), (1,2), (0,3), (2,2), (2,3), (1,1), (1,0)}) # testing from 2 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (2,3)), {(1,3), (1,2), (2,2), (0,3), (0,1), (2,1)}) # testing from 3 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (0,2)), {(0,3), (0,1), (1,3), (1,2), (1,1), (2,2)}) # testing from 4 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (1,2)), {(0,3), (0,2), (0,1), (1,3), (1,1), (2,3), (2,2), (2,1), (1,0)}) # testing from 5 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (2,2)), {(2,3), (2,1), (1,3), (1,2), (1,1), (0,2)}) # testing from 6 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (0,1)), {(0,2), (1,2), (1,1), (1,0), (0,3), (2,1), (2,3)}) # testing from 7 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (1,1)), {(0,1), (0,2), (1,2), (1,0), (2,2), (2,1), (1,3)}) # testing from 8 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (2,1)), {(2,2), (1,0), (1,1), (1,2), (2,3), (0,3), (0,1)}) # testing from 9 position 
        self.assertEqual(phoneChess.queen.calculateAvailableMoves(board, (1,0)), {(0,1), (1,1), (2,1), (1,2), (1,3)}) # testing from 0 position 

    def test_calculateAvailableMoves_Bishop(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for bishop chess piece

        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (0,3)), {(1,2), (2,1)}) # testing from 1 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (1,3)), {(0,2), (2,2)}) # testing from 2 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (2,3)), {(1,2), (0,1)}) # testing from 3 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (0,2)), {(1,3), (1,1)}) # testing from 4 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (1,2)), {(0,3), (0,1), (2,3), (2,1)}) # testing from 5 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (2,2)), {(1,3), (1,1)}) # testing from 6 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (0,1)), {(1,2), (2,3), (1,0)}) # testing from 7 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (1,1)), {(0,2), (2,2)}) # testing from 8 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (2,1)), {(1,2), (0,3), (1,0)}) # testing from 9 position 
        self.assertEqual(phoneChess.bishop.calculateAvailableMoves(board, (1,0)), {(0,1), (2,1)}) # testing from 0 position

    def test_calculateAvailableMoves_Rook(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for rook chess piece

        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (0,3)), {(0,2), (0,1), (1,3), (2,3)}) # testing from 1 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (1,3)), {(0,3), (2,3), (1,2), (1,1), (1,0)}) # testing from 2 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (2,3)), {(0,3), (1,3), (2,2), (2,1)}) # testing from 3 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (0,2)), {(1,2), (2,2), (0,3), (0,1)}) # testing from 4 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (1,2)), {(1,3), (1,1), (1,0), (2,2), (0,2)}) # testing from 5 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (2,2)), {(2,3), (2,1), (0,2), (1,2)}) # testing from 6 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (0,1)), {(0,2), (0,3), (1,1), (2,1)}) # testing from 7 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (1,1)), {(1,0), (1,2), (1,3), (0,1), (2,1)}) # testing from 8 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (2,1)), {(1,1), (0,1), (2,2), (2,3)}) # testing from 9 position 
        self.assertEqual(phoneChess.rook.calculateAvailableMoves(board, (1,0)), {(1,1), (1,2), (1,3)}) # testing from 0 position 

    def test_calculateAvailableMoves_Knight(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for knight chess piece

        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (0,3)), {(1,1), (2,2)}) # testing from 1 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (1,3)), {(0,1), (2,1)}) # testing from 2 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (2,3)), {(0,2), (1,1)}) # testing from 3 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (0,2)), {(2,3), (2,1), (1,0)}) # testing from 4 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (1,2)), set()) # testing from 5 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (2,2)), {(0,3), (0,1), (1,0)}) # testing from 6 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (0,1)), {(1,3), (2,2)}) # testing from 7 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (1,1)), {(0,3), (2,3)}) # testing from 8 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (2,1)), {(1,3), (0,2)}) # testing from 9 position 
        self.assertEqual(phoneChess.knight.calculateAvailableMoves(board, (1,0)), {(0,2), (2,2)}) # testing from 0 position 

    def test_calculateAvailableMoves_Pawn(self):

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # testing moves for pawn chess piece that is on their first move
        pawn = phoneChess.pawn #  represents the pawn piece

        self.assertEqual(pawn.calculateAvailableMoves(board, (0,3)), set()) # testing from 1 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,3)), set()) # testing from 2 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,3)), set()) # testing from 3 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (0,2)), {(0,3)}) # testing from 4 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,2)), {(1,3)}) # testing from 5 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,2)), {(2,3)}) # testing from 6 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (0,1)), {(0,2), (0,3)}) # testing from 7 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,1)), {(1,2), (1,3)}) # testing from 8 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,1)), {(2,2), (2,3)}) # testing from 9 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,0)), {(1,1), (1,2)}) # testing from 0 position 

        pawn.madeFirstMove = True # new tests for when the pawn has made their first move already

        self.assertEqual(pawn.calculateAvailableMoves(board, (0,3)), set()) # testing from 1 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,3)), set()) # testing from 2 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,3)), set()) # testing from 3 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (0,2)), {(0,3)}) # testing from 4 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,2)), {(1,3)}) # testing from 5 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,2)), {(2,3)}) # testing from 6 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (0,1)), {(0,2)}) # testing from 7 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,1)), {(1,2)}) # testing from 8 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (2,1)), {(2,2)}) # testing from 9 position 
        self.assertEqual(pawn.calculateAvailableMoves(board, (1,0)), {(1,1)}) # testing from 0 position 

    def test_boardIsSqaureValid(self):
        # testing the board class method that checks if a board square is valid to move to

        # an invalid board square is either a square that is not within the board's boundaries, or a square that has been manually marked as invalid

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # valid squares: this is all of the squares on the keypad, except for the '#' and '*' squares
        self.assertTrue(board.isSquareValid((0,3)))
        self.assertTrue(board.isSquareValid((1,3)))
        self.assertTrue(board.isSquareValid((2,3)))
        self.assertTrue(board.isSquareValid((0,2)))
        self.assertTrue(board.isSquareValid((1,2)))
        self.assertTrue(board.isSquareValid((2,2)))
        self.assertTrue(board.isSquareValid((0,1)))
        self.assertTrue(board.isSquareValid((1,1)))
        self.assertTrue(board.isSquareValid((2,1)))
        self.assertTrue(board.isSquareValid((1,0)))

        # invalid squares: this tests to make sure the '*' and '#' squares are invalid, and also tests squares that shouldn't exist on the board
        self.assertFalse(board.isSquareValid((0,0)))
        self.assertFalse(board.isSquareValid((2,0)))
        self.assertFalse(board.isSquareValid((-1,1)))
        self.assertFalse(board.isSquareValid((1,-1)))
        self.assertFalse(board.isSquareValid((-1,-1)))
        self.assertFalse(board.isSquareValid((3, 4)))
        self.assertFalse(board.isSquareValid((1,4)))
        self.assertFalse(board.isSquareValid((-1,4)))
        self.assertFalse(board.isSquareValid((200,100)))
        self.assertFalse(board.isSquareValid((5,2)))
        self.assertFalse(board.isSquareValid((5,-1)))



    def test_boardGetRange(self):
        # testing the getRange method from the board class

        board = phoneChess.phoneBoard # this represents the phone keypad board

        # an infinite movement range, should return a range that goes from 0, to the edge of the board
        self.assertEqual(board.getRange(inf, 1, "horizontal"), range(0, 3)) # this range includes, 0, 1, and 2. the 3 is not included, so this is the correct range
        self.assertEqual(board.getRange(inf, 2, "vertical"), range(0, 4))
        
        # a movement range of 1, should return a range between the current position-1, and the current position+1
        self.assertEqual(board.getRange(1, 1, "horizontal"), range(0, 3))
        self.assertEqual(board.getRange(1, 2, "vertical"), range(1, 4))

        self.assertEqual(board.getRange(99, 1, "horizontal"), range(0, 3))
        self.assertEqual(board.getRange(99, 2, "vertical"), range(0, 4))

        self.assertRaises(IndexError, board.getRange, -3, 2, "horizontal")
        self.assertRaises(ValueError, board.getRange, 2, 2, "a")

    def test_boardGetLocationValue(self):
        
        # this tests each coordinate to see if if returns the correct value

        board = phoneChess.phoneBoard # this represents the phone keypad board

        self.assertEqual(board.getLocationValue((0,3)), '1')
        self.assertEqual(board.getLocationValue((1,3)), '2')
        self.assertEqual(board.getLocationValue((2,3)), '3')
        self.assertEqual(board.getLocationValue((0,2)), '4')
        self.assertEqual(board.getLocationValue((1,2)), '5')
        self.assertEqual(board.getLocationValue((2,2)), '6')
        self.assertEqual(board.getLocationValue((0,1)), '7')
        self.assertEqual(board.getLocationValue((1,1)), '8')
        self.assertEqual(board.getLocationValue((2,1)), '9')
        self.assertEqual(board.getLocationValue((0,0)), '*')
        self.assertEqual(board.getLocationValue((1,0)), '0')
        self.assertEqual(board.getLocationValue((2,0)), '#')

        self.assertRaises(IndexError, board.getLocationValue, (2,4)) # this should raise an error since its out of range
        




if __name__ == '__main__':
    unittest.main()