from abaloneAI.board import board
import numpy as np

b = board()

key = np.array(((6, 6), (5, 7), (4, 8)),dtype='i1')
pos = np.array((4, 8),dtype='i1')
move = np.array(((6, 5), (5, 6), (4, 7)),dtype='i1')
color = 2
