import abaloneAI.board as br
import unittest
import numpy as np

b = br.board()
key = np.array(((6, 6), (5, 7), (4, 8)),dtype='i1')
pos = np.array((4, 8),dtype='i1')
move = np.array(((6, 5), (5, 6), (4, 7)),dtype='i1')
color = 2

class board_test(unittest.TestCase):
    def test_opsite(self):
        self.assertEqual(br.opsite(color) ,3)

    def test_on_key(self):
        self.assertTrue(br.on_key(key,pos))
    
    def test_on_board(self):
        self.assertFalse(on_board(key,color))
    
    def test_get_dir(self):
        self.assertEqual(br.get_dir(key,move) ,np.array((0,-1),dtype='i1'))

    def test_move_type(self):
        self.assertTrue(br.move_type(key,move))

    def test_legal_move(self):
        self.assertFalse(br.legal_move(key,move,color))

if __name__ == '__main__':
    unittest.main()

assert br.opsite(color) == 3
assert br.on_key(key,pos) == True
assert br.on_board(key,color) == False
assert br.get_dir(key,move) == np.array((0,-1),dtype='i1')
assert br.move_type(key,move) == True
assert br.legal_move(key,move,color) == False
