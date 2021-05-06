import unittest
import phoneChess

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

if __name__ == '__main__':
    unittest.main()