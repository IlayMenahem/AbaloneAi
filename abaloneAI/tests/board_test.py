import abaloneAI.board as br
import numpy as np

b = br.board()

key = np.array(((6, 6), (5, 7), (4, 8)),dtype='i1')
pos = np.array((4, 8),dtype='i1')
move = np.array(((6, 5), (5, 6), (4, 7)),dtype='i1')
color = 2

assert br.opsite(color) == 3
assert br.on_key(key,pos) == True
assert br.on_board(key,color) == False
assert br.get_dir(key,move) == np.array((0,-1),dtype='i1')
assert br.move_type(key,move) == True
assert br.legal_move(key,move,color) == False
