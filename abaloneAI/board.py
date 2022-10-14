# TODO:
# make a game with gui
# make dictionary creator
# test all current functions
# enable game actions
# enable njit if reasonable

from numba import njit
import numpy as np

class board:
    """
    counstracts a new board
    """
    def __init__(self):
        # board
        # none = 0 empty = 1, white = 2, black = 3
        self.entries = np.array(
            [
                [2, 2, 2, 2, 2, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 0, 0, 0],
                [1, 1, 2, 2, 2, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 3, 3, 3, 1, 1, 0, 0],
                [3, 3, 3, 3, 3, 3, 0, 0, 0],
                [3, 3, 3, 3, 3, 0, 0, 0, 0],
            ],
            dtype='i1',
        )

        #possible positions
        self.pos1 = {}
        self.pos2 = {}
        self.pos3 = np.array({((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 1), (0, 2), (0, 3)),
        ((0, 1), (1, 2), (2, 3)),
        ((0, 2), (0, 3), (0, 4)),
        ((0, 2), (1, 3), (2, 4)),
        ((0, 3), (1, 4), (2, 5)),
        ((0, 4), (1, 5), (2, 6)),
        ((1, 0), (1, 1), (1, 2)),
        ((1, 0), (2, 1), (3, 2)),
        ((1, 1), (1, 2), (1, 3)),
        ((1, 1), (2, 2), (3, 3)),
        ((1, 2), (1, 3), (1, 4)),
        ((1, 2), (2, 3), (3, 4)),
        ((1, 3), (1, 4), (1, 5)),
        ((1, 3), (2, 4), (3, 5)),
        ((1, 4), (2, 5), (3, 6)),
        ((1, 5), (2, 6), (3, 7)),
        ((2, 0), (1, 0), (0, 0)),
        ((2, 0), (2, 1), (2, 2)),
        ((2, 0), (3, 1), (4, 2)),
        ((2, 1), (1, 1), (0, 1)),
        ((2, 1), (2, 2), (2, 3)),
        ((2, 1), (3, 2), (4, 3)),
        ((2, 2), (1, 2), (0, 2)),
        ((2, 2), (2, 3), (2, 4)),
        ((2, 2), (3, 3), (4, 4)),
        ((2, 3), (1, 3), (0, 3)),
        ((2, 3), (2, 4), (2, 5)),
        ((2, 3), (3, 4), (4, 5)),
        ((2, 4), (1, 4), (0, 4)),
        ((2, 4), (2, 5), (2, 6)),
        ((2, 4), (3, 5), (4, 6)),
        ((2, 5), (3, 6), (4, 7)),
        ((2, 6), (3, 7), (4, 8)),
        ((3, 0), (2, 0), (1, 0)),
        ((3, 0), (3, 1), (3, 2)),
        ((3, 0), (4, 1), (5, 1)),
        ((3, 1), (2, 1), (1, 1)),
        ((3, 1), (3, 2), (3, 3)),
        ((3, 1), (4, 2), (5, 2)),
        ((3, 2), (2, 2), (1, 2)),
        ((3, 2), (3, 3), (3, 4)),
        ((3, 2), (4, 3), (5, 3)),
        ((3, 3), (2, 3), (1, 3)),
        ((3, 3), (3, 4), (3, 5)),
        ((3, 3), (4, 4), (5, 4)),
        ((3, 4), (2, 4), (1, 4)),
        ((3, 4), (3, 5), (3, 6)),
        ((3, 4), (4, 5), (5, 5)),
        ((3, 5), (2, 5), (1, 5)),
        ((3, 5), (3, 6), (3, 7)),
        ((3, 5), (4, 6), (5, 6)),
        ((3, 6), (4, 7), (5, 7)),
        ((4, 0), (3, 0), (2, 0)),
        ((4, 0), (4, 1), (4, 2)),
        ((4, 0), (5, 0), (6, 0)),
        ((4, 1), (3, 1), (2, 1)),
        ((4, 1), (4, 2), (4, 3)),
        ((4, 1), (5, 1), (6, 1)),
        ((4, 2), (3, 2), (2, 2)),
        ((4, 2), (4, 3), (4, 4)),
        ((4, 2), (5, 2), (6, 2)),
        ((4, 3), (3, 3), (2, 3)),
        ((4, 3), (4, 4), (4, 5)),
        ((4, 3), (5, 3), (6, 3)),
        ((4, 4), (3, 4), (2, 4)),
        ((4, 4), (4, 5), (4, 6)),
        ((4, 4), (5, 4), (6, 4)),
        ((4, 5), (3, 5), (2, 5)),
        ((4, 5), (4, 6), (4, 7)),
        ((4, 5), (5, 5), (6, 5)),
        ((4, 6), (3, 6), (2, 6)),
        ((4, 6), (4, 7), (4, 8)),
        ((4, 6), (5, 6), (6, 6)),
        ((5, 0), (4, 1), (3, 1)),
        ((5, 0), (5, 1), (5, 2)),
        ((5, 0), (6, 0), (7, 0)),
        ((5, 1), (4, 2), (3, 2)),
        ((5, 1), (5, 2), (5, 3)),
        ((5, 1), (6, 1), (7, 1)),
        ((5, 2), (4, 3), (3, 3)),
        ((5, 2), (5, 3), (5, 4)),
        ((5, 2), (6, 2), (7, 2)),
        ((5, 3), (4, 4), (3, 4)),
        ((5, 3), (5, 4), (5, 5)),
        ((5, 3), (6, 3), (7, 3)),
        ((5, 4), (4, 5), (3, 5)),
        ((5, 4), (5, 5), (5, 6)),
        ((5, 4), (6, 4), (7, 4)),
        ((5, 5), (4, 6), (3, 6)),
        ((5, 5), (5, 6), (5, 7)),
        ((5, 5), (6, 5), (7, 5)),
        ((5, 6), (4, 7), (3, 7)),
        ((6, 0), (5, 1), (4, 2)),
        ((6, 0), (6, 1), (6, 2)),
        ((6, 0), (7, 0), (8, 0)),
        ((6, 1), (5, 2), (4, 3)),
        ((6, 1), (6, 2), (6, 3)),
        ((6, 1), (7, 1), (8, 1)),
        ((6, 2), (5, 3), (4, 4)),
        ((6, 2), (6, 3), (6, 4)),
        ((6, 2), (7, 2), (8, 2)),
        ((6, 3), (5, 4), (4, 5)),
        ((6, 3), (6, 4), (6, 5)),
        ((6, 3), (7, 3), (8, 3)),
        ((6, 4), (5, 5), (4, 6)),
        ((6, 4), (6, 5), (6, 6)),
        ((6, 4), (7, 4), (8, 4)),
        ((6, 5), (5, 6), (4, 7)),
        ((6, 6), (5, 7), (4, 8)),
        ((7, 0), (6, 1), (5, 2)),
        ((7, 0), (7, 1), (7, 2)),
        ((7, 1), (6, 2), (5, 3)),
        ((7, 1), (7, 2), (7, 3)),
        ((7, 2), (6, 3), (5, 4)),
        ((7, 2), (7, 3), (7, 4)),
        ((7, 3), (6, 4), (5, 5)),
        ((7, 3), (7, 4), (7, 5)),
        ((7, 4), (6, 5), (5, 6)),
        ((7, 5), (6, 6), (5, 7)),
        ((8, 0), (7, 1), (6, 2)),
        ((8, 0), (8, 1), (8, 2)),
        ((8, 1), (7, 2), (6, 3)),
        ((8, 1), (8, 2), (8, 3)),
        ((8, 2), (7, 3), (6, 4)),
        ((8, 2), (8, 3), (8, 4)),
        ((8, 3), (7, 4), (6, 5)),
        ((8, 4), (7, 5), (6, 6))}, dtype= 'i1')

        # possible moves
        self.moves_black = {}
        self.moves_white = {}

        self.moves = {((6, 6), (5, 7), (4, 8)): [((6, 5), (5, 6), (4, 7)),
        ((5, 6), (4, 7), (3, 7)),
        ((7, 5), (6, 6), (5, 7))],
        ((6, 0), (5, 1), (4, 2)): [((6, 1), (5, 2), (4, 3)),
        ((5, 1), (4, 2), (3, 2)),
        ((5, 0), (4, 1), (3, 1)),
        ((7, 0), (6, 1), (5, 2))],
        ((6, 4), (6, 5), (6, 6)): [((6, 3), (6, 4), (6, 5)),
        ((5, 5), (5, 6), (5, 7)),
        ((5, 4), (5, 5), (5, 6)),
        ((7, 3), (7, 4), (7, 5))],
        ((4, 6), (5, 6), (6, 6)): [((4, 5), (5, 5), (6, 5)),
        ((3, 6), (4, 7), (5, 7)),
        ((3, 5), (4, 6), (5, 6)),
        ((5, 5), (6, 5), (7, 5))],
        ((1, 2), (2, 3), (3, 4)): [((1, 3), (2, 4), (3, 5)),
        ((1, 1), (2, 2), (3, 3)),
        ((0, 2), (1, 3), (2, 4)),
        ((0, 1), (1, 2), (2, 3)),
        ((2, 3), (3, 4), (4, 5)),
        ((2, 2), (3, 3), (4, 4))],
        ((1, 1), (1, 2), (1, 3)): [((1, 2), (1, 3), (1, 4)),
        ((1, 0), (1, 1), (1, 2)),
        ((0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (0, 2)),
        ((2, 2), (2, 3), (2, 4)),
        ((2, 1), (2, 2), (2, 3))],
        ((6, 5), (5, 6), (4, 7)): [((6, 6), (5, 7), (4, 8)),
        ((6, 4), (5, 5), (4, 6)),
        ((5, 6), (4, 7), (3, 7)),
        ((5, 5), (4, 6), (3, 6)),
        ((7, 5), (6, 6), (5, 7)),
        ((7, 4), (6, 5), (5, 6))],
        ((7, 1), (6, 2), (5, 3)): [((7, 2), (6, 3), (5, 4)),
        ((7, 0), (6, 1), (5, 2)),
        ((6, 2), (5, 3), (4, 4)),
        ((6, 1), (5, 2), (4, 3)),
        ((8, 1), (7, 2), (6, 3)),
        ((8, 0), (7, 1), (6, 2))],
        ((7, 3), (7, 4), (7, 5)): [((7, 2), (7, 3), (7, 4)),
        ((6, 4), (6, 5), (6, 6)),
        ((6, 3), (6, 4), (6, 5)),
        ((8, 2), (8, 3), (8, 4))],
        ((2, 1), (2, 2), (2, 3)): [((2, 2), (2, 3), (2, 4)),
        ((2, 0), (2, 1), (2, 2)),
        ((1, 1), (1, 2), (1, 3)),
        ((1, 0), (1, 1), (1, 2)),
        ((3, 2), (3, 3), (3, 4)),
        ((3, 1), (3, 2), (3, 3))],
        ((4, 6), (4, 7), (4, 8)): [((4, 5), (4, 6), (4, 7)),
        ((3, 5), (3, 6), (3, 7)),
        ((5, 5), (5, 6), (5, 7))],
        ((3, 1), (2, 1), (1, 1)): [((3, 2), (2, 2), (1, 2)),
        ((3, 0), (2, 0), (1, 0)),
        ((2, 1), (1, 1), (0, 1)),
        ((2, 0), (1, 0), (0, 0)),
        ((4, 2), (3, 2), (2, 2)),
        ((4, 1), (3, 1), (2, 1))],
        ((6, 0), (6, 1), (6, 2)): [((6, 1), (6, 2), (6, 3)),
        ((5, 1), (5, 2), (5, 3)),
        ((5, 0), (5, 1), (5, 2)),
        ((7, 0), (7, 1), (7, 2))],
        ((2, 2), (3, 3), (4, 4)): [((2, 3), (3, 4), (4, 5)),
        ((2, 1), (3, 2), (4, 3)),
        ((1, 2), (2, 3), (3, 4)),
        ((1, 1), (2, 2), (3, 3)),
        ((3, 3), (4, 4), (5, 4)),
        ((3, 2), (4, 3), (5, 3))],
        ((2, 3), (3, 4), (4, 5)): [((2, 4), (3, 5), (4, 6)),
        ((2, 2), (3, 3), (4, 4)),
        ((1, 3), (2, 4), (3, 5)),
        ((1, 2), (2, 3), (3, 4)),
        ((3, 4), (4, 5), (5, 5)),
        ((3, 3), (4, 4), (5, 4))],
        ((4, 0), (3, 0), (2, 0)): [((4, 1), (3, 1), (2, 1)),
        ((3, 0), (2, 0), (1, 0)),
        ((5, 0), (4, 1), (3, 1))],
        ((1, 2), (1, 3), (1, 4)): [((1, 3), (1, 4), (1, 5)),
        ((1, 1), (1, 2), (1, 3)),
        ((0, 2), (0, 3), (0, 4)),
        ((0, 1), (0, 2), (0, 3)),
        ((2, 3), (2, 4), (2, 5)),
        ((2, 2), (2, 3), (2, 4))],
        ((2, 1), (1, 1), (0, 1)): [((2, 2), (1, 2), (0, 2)),
        ((2, 0), (1, 0), (0, 0)),
        ((3, 2), (2, 2), (1, 2)),
        ((3, 1), (2, 1), (1, 1))],
        ((4, 3), (3, 3), (2, 3)): [((4, 4), (3, 4), (2, 4)),
        ((4, 2), (3, 2), (2, 2)),
        ((3, 3), (2, 3), (1, 3)),
        ((3, 2), (2, 2), (1, 2)),
        ((5, 3), (4, 4), (3, 4)),
        ((5, 2), (4, 3), (3, 3))],
        ((6, 2), (7, 2), (8, 2)): [((6, 3), (7, 3), (8, 3)),
        ((6, 1), (7, 1), (8, 1)),
        ((5, 3), (6, 3), (7, 3)),
        ((5, 2), (6, 2), (7, 2))],
        ((2, 1), (3, 2), (4, 3)): [((2, 2), (3, 3), (4, 4)),
        ((2, 0), (3, 1), (4, 2)),
        ((1, 1), (2, 2), (3, 3)),
        ((1, 0), (2, 1), (3, 2)),
        ((3, 2), (4, 3), (5, 3)),
        ((3, 1), (4, 2), (5, 2))],
        ((0, 1), (0, 2), (0, 3)): [((0, 2), (0, 3), (0, 4)),
        ((0, 0), (0, 1), (0, 2)),
        ((1, 2), (1, 3), (1, 4)),
        ((1, 1), (1, 2), (1, 3))],
        ((8, 0), (7, 1), (6, 2)): [((8, 1), (7, 2), (6, 3)),
        ((7, 1), (6, 2), (5, 3)),
        ((7, 0), (6, 1), (5, 2))],
        ((6, 4), (7, 4), (8, 4)): [((6, 3), (7, 3), (8, 3)),
        ((5, 5), (6, 5), (7, 5)),
        ((5, 4), (6, 4), (7, 4))],
        ((3, 2), (2, 2), (1, 2)): [((3, 3), (2, 3), (1, 3)),
        ((3, 1), (2, 1), (1, 1)),
        ((2, 2), (1, 2), (0, 2)),
        ((2, 1), (1, 1), (0, 1)),
        ((4, 3), (3, 3), (2, 3)),
        ((4, 2), (3, 2), (2, 2))],
        ((0, 3), (1, 4), (2, 5)): [((0, 4), (1, 5), (2, 6)),
        ((0, 2), (1, 3), (2, 4)),
        ((1, 4), (2, 5), (3, 6)),
        ((1, 3), (2, 4), (3, 5))],
        ((7, 2), (7, 3), (7, 4)): [((7, 3), (7, 4), (7, 5)),
        ((7, 1), (7, 2), (7, 3)),
        ((6, 3), (6, 4), (6, 5)),
        ((6, 2), (6, 3), (6, 4)),
        ((8, 2), (8, 3), (8, 4)),
        ((8, 1), (8, 2), (8, 3))],
        ((4, 4), (3, 4), (2, 4)): [((4, 5), (3, 5), (2, 5)),
        ((4, 3), (3, 3), (2, 3)),
        ((3, 4), (2, 4), (1, 4)),
        ((3, 3), (2, 3), (1, 3)),
        ((5, 4), (4, 5), (3, 5)),
        ((5, 3), (4, 4), (3, 4))],
        ((3, 5), (4, 6), (5, 6)): [((3, 6), (4, 7), (5, 7)),
        ((3, 4), (4, 5), (5, 5)),
        ((2, 5), (3, 6), (4, 7)),
        ((2, 4), (3, 5), (4, 6)),
        ((4, 6), (5, 6), (6, 6)),
        ((4, 5), (5, 5), (6, 5))],
        ((6, 3), (5, 4), (4, 5)): [((6, 4), (5, 5), (4, 6)),
        ((6, 2), (5, 3), (4, 4)),
        ((5, 4), (4, 5), (3, 5)),
        ((5, 3), (4, 4), (3, 4)),
        ((7, 3), (6, 4), (5, 5)),
        ((7, 2), (6, 3), (5, 4))],
        ((3, 1), (3, 2), (3, 3)): [((3, 2), (3, 3), (3, 4)),
        ((3, 0), (3, 1), (3, 2)),
        ((2, 1), (2, 2), (2, 3)),
        ((2, 0), (2, 1), (2, 2)),
        ((4, 2), (4, 3), (4, 4)),
        ((4, 1), (4, 2), (4, 3))],
        ((6, 1), (5, 2), (4, 3)): [((6, 2), (5, 3), (4, 4)),
        ((6, 0), (5, 1), (4, 2)),
        ((5, 2), (4, 3), (3, 3)),
        ((5, 1), (4, 2), (3, 2)),
        ((7, 1), (6, 2), (5, 3)),
        ((7, 0), (6, 1), (5, 2))],
        ((0, 2), (1, 3), (2, 4)): [((0, 3), (1, 4), (2, 5)),
        ((0, 1), (1, 2), (2, 3)),
        ((1, 3), (2, 4), (3, 5)),
        ((1, 2), (2, 3), (3, 4))],
        ((4, 2), (5, 2), (6, 2)): [((4, 3), (5, 3), (6, 3)),
        ((4, 1), (5, 1), (6, 1)),
        ((3, 2), (4, 3), (5, 3)),
        ((3, 1), (4, 2), (5, 2)),
        ((5, 2), (6, 2), (7, 2)),
        ((5, 1), (6, 1), (7, 1))],
        ((1, 1), (2, 2), (3, 3)): [((1, 2), (2, 3), (3, 4)),
        ((1, 0), (2, 1), (3, 2)),
        ((0, 1), (1, 2), (2, 3)),
        ((0, 0), (1, 1), (2, 2)),
        ((2, 2), (3, 3), (4, 4)),
        ((2, 1), (3, 2), (4, 3))],
        ((1, 0), (2, 1), (3, 2)): [((1, 1), (2, 2), (3, 3)),
        ((0, 0), (1, 1), (2, 2)),
        ((2, 1), (3, 2), (4, 3)),
        ((2, 0), (3, 1), (4, 2))],
        ((1, 4), (2, 5), (3, 6)): [((1, 5), (2, 6), (3, 7)),
        ((1, 3), (2, 4), (3, 5)),
        ((0, 4), (1, 5), (2, 6)),
        ((0, 3), (1, 4), (2, 5)),
        ((2, 5), (3, 6), (4, 7)),
        ((2, 4), (3, 5), (4, 6))],
        ((6, 3), (6, 4), (6, 5)): [((6, 4), (6, 5), (6, 6)),
        ((6, 2), (6, 3), (6, 4)),
        ((5, 4), (5, 5), (5, 6)),
        ((5, 3), (5, 4), (5, 5)),
        ((7, 3), (7, 4), (7, 5)),
        ((7, 2), (7, 3), (7, 4))],
        ((1, 3), (2, 4), (3, 5)): [((1, 4), (2, 5), (3, 6)),
        ((1, 2), (2, 3), (3, 4)),
        ((0, 3), (1, 4), (2, 5)),
        ((0, 2), (1, 3), (2, 4)),
        ((2, 4), (3, 5), (4, 6)),
        ((2, 3), (3, 4), (4, 5))],
        ((4, 1), (5, 1), (6, 1)): [((4, 2), (5, 2), (6, 2)),
        ((4, 0), (5, 0), (6, 0)),
        ((3, 1), (4, 2), (5, 2)),
        ((3, 0), (4, 1), (5, 1)),
        ((5, 1), (6, 1), (7, 1)),
        ((5, 0), (6, 0), (7, 0))],
        ((7, 2), (6, 3), (5, 4)): [((7, 3), (6, 4), (5, 5)),
        ((7, 1), (6, 2), (5, 3)),
        ((6, 3), (5, 4), (4, 5)),
        ((6, 2), (5, 3), (4, 4)),
        ((8, 2), (7, 3), (6, 4)),
        ((8, 1), (7, 2), (6, 3))],
        ((4, 0), (4, 1), (4, 2)): [((4, 1), (4, 2), (4, 3)),
        ((3, 0), (3, 1), (3, 2)),
        ((5, 0), (5, 1), (5, 2))],
        ((4, 3), (4, 4), (4, 5)): [((4, 4), (4, 5), (4, 6)),
        ((4, 2), (4, 3), (4, 4)),
        ((3, 3), (3, 4), (3, 5)),
        ((3, 2), (3, 3), (3, 4)),
        ((5, 3), (5, 4), (5, 5)),
        ((5, 2), (5, 3), (5, 4))],
        ((1, 5), (2, 6), (3, 7)): [((1, 4), (2, 5), (3, 6)),
        ((0, 4), (1, 5), (2, 6)),
        ((2, 6), (3, 7), (4, 8)),
        ((2, 5), (3, 6), (4, 7))],
        ((4, 5), (3, 5), (2, 5)): [((4, 6), (3, 6), (2, 6)),
        ((4, 4), (3, 4), (2, 4)),
        ((3, 5), (2, 5), (1, 5)),
        ((3, 4), (2, 4), (1, 4)),
        ((5, 5), (4, 6), (3, 6)),
        ((5, 4), (4, 5), (3, 5))],
        ((8, 2), (7, 3), (6, 4)): [((8, 3), (7, 4), (6, 5)),
        ((8, 1), (7, 2), (6, 3)),
        ((7, 3), (6, 4), (5, 5)),
        ((7, 2), (6, 3), (5, 4))],
        ((6, 2), (6, 3), (6, 4)): [((6, 3), (6, 4), (6, 5)),
        ((6, 1), (6, 2), (6, 3)),
        ((5, 3), (5, 4), (5, 5)),
        ((5, 2), (5, 3), (5, 4)),
        ((7, 2), (7, 3), (7, 4)),
        ((7, 1), (7, 2), (7, 3))],
        ((6, 0), (7, 0), (8, 0)): [((6, 1), (7, 1), (8, 1)),
        ((5, 1), (6, 1), (7, 1)),
        ((5, 0), (6, 0), (7, 0))],
        ((8, 1), (8, 2), (8, 3)): [((8, 2), (8, 3), (8, 4)),
        ((8, 0), (8, 1), (8, 2)),
        ((7, 2), (7, 3), (7, 4)),
        ((7, 1), (7, 2), (7, 3))],
        ((4, 2), (3, 2), (2, 2)): [((4, 3), (3, 3), (2, 3)),
        ((4, 1), (3, 1), (2, 1)),
        ((3, 2), (2, 2), (1, 2)),
        ((3, 1), (2, 1), (1, 1)),
        ((5, 2), (4, 3), (3, 3)),
        ((5, 1), (4, 2), (3, 2))],
        ((5, 3), (6, 3), (7, 3)): [((5, 4), (6, 4), (7, 4)),
        ((5, 2), (6, 2), (7, 2)),
        ((4, 4), (5, 4), (6, 4)),
        ((4, 3), (5, 3), (6, 3)),
        ((6, 3), (7, 3), (8, 3)),
        ((6, 2), (7, 2), (8, 2))],
        ((1, 3), (1, 4), (1, 5)): [((1, 2), (1, 3), (1, 4)),
        ((0, 2), (0, 3), (0, 4)),
        ((2, 4), (2, 5), (2, 6)),
        ((2, 3), (2, 4), (2, 5))],
        ((4, 0), (5, 0), (6, 0)): [((4, 1), (5, 1), (6, 1)),
        ((3, 0), (4, 1), (5, 1)),
        ((5, 0), (6, 0), (7, 0))],
        ((8, 2), (8, 3), (8, 4)): [((8, 1), (8, 2), (8, 3)),
        ((7, 3), (7, 4), (7, 5)),
        ((7, 2), (7, 3), (7, 4))],
        ((8, 4), (7, 5), (6, 6)): [((8, 3), (7, 4), (6, 5)),
        ((7, 5), (6, 6), (5, 7)),
        ((7, 4), (6, 5), (5, 6))],
        ((3, 6), (4, 7), (5, 7)): [((3, 5), (4, 6), (5, 6)),
        ((2, 6), (3, 7), (4, 8)),
        ((2, 5), (3, 6), (4, 7)),
        ((4, 6), (5, 6), (6, 6))],
        ((7, 4), (6, 5), (5, 6)): [((7, 5), (6, 6), (5, 7)),
        ((7, 3), (6, 4), (5, 5)),
        ((6, 5), (5, 6), (4, 7)),
        ((6, 4), (5, 5), (4, 6)),
        ((8, 4), (7, 5), (6, 6)),
        ((8, 3), (7, 4), (6, 5))],
        ((2, 5), (3, 6), (4, 7)): [((2, 6), (3, 7), (4, 8)),
        ((2, 4), (3, 5), (4, 6)),
        ((1, 5), (2, 6), (3, 7)),
        ((1, 4), (2, 5), (3, 6)),
        ((3, 6), (4, 7), (5, 7)),
        ((3, 5), (4, 6), (5, 6))],
        ((0, 0), (1, 1), (2, 2)): [((0, 1), (1, 2), (2, 3)),
        ((1, 1), (2, 2), (3, 3)),
        ((1, 0), (2, 1), (3, 2))],
        ((5, 3), (5, 4), (5, 5)): [((5, 4), (5, 5), (5, 6)),
        ((5, 2), (5, 3), (5, 4)),
        ((4, 4), (4, 5), (4, 6)),
        ((4, 3), (4, 4), (4, 5)),
        ((6, 3), (6, 4), (6, 5)),
        ((6, 2), (6, 3), (6, 4))],
        ((0, 1), (1, 2), (2, 3)): [((0, 2), (1, 3), (2, 4)),
        ((0, 0), (1, 1), (2, 2)),
        ((1, 2), (2, 3), (3, 4)),
        ((1, 1), (2, 2), (3, 3))],
        ((2, 4), (3, 5), (4, 6)): [((2, 5), (3, 6), (4, 7)),
        ((2, 3), (3, 4), (4, 5)),
        ((1, 4), (2, 5), (3, 6)),
        ((1, 3), (2, 4), (3, 5)),
        ((3, 5), (4, 6), (5, 6)),
        ((3, 4), (4, 5), (5, 5))],
        ((5, 4), (5, 5), (5, 6)): [((5, 5), (5, 6), (5, 7)),
        ((5, 3), (5, 4), (5, 5)),
        ((4, 5), (4, 6), (4, 7)),
        ((4, 4), (4, 5), (4, 6)),
        ((6, 4), (6, 5), (6, 6)),
        ((6, 3), (6, 4), (6, 5))],
        ((3, 0), (2, 0), (1, 0)): [((3, 1), (2, 1), (1, 1)),
        ((2, 0), (1, 0), (0, 0)),
        ((4, 1), (3, 1), (2, 1)),
        ((4, 0), (3, 0), (2, 0))],
        ((4, 4), (5, 4), (6, 4)): [((4, 5), (5, 5), (6, 5)),
        ((4, 3), (5, 3), (6, 3)),
        ((3, 4), (4, 5), (5, 5)),
        ((3, 3), (4, 4), (5, 4)),
        ((5, 4), (6, 4), (7, 4)),
        ((5, 3), (6, 3), (7, 3))],
        ((7, 0), (6, 1), (5, 2)): [((7, 1), (6, 2), (5, 3)),
        ((6, 1), (5, 2), (4, 3)),
        ((6, 0), (5, 1), (4, 2)),
        ((8, 0), (7, 1), (6, 2))],
        ((4, 1), (4, 2), (4, 3)): [((4, 2), (4, 3), (4, 4)),
        ((4, 0), (4, 1), (4, 2)),
        ((3, 1), (3, 2), (3, 3)),
        ((3, 0), (3, 1), (3, 2)),
        ((5, 1), (5, 2), (5, 3)),
        ((5, 0), (5, 1), (5, 2))],
        ((5, 5), (5, 6), (5, 7)): [((5, 4), (5, 5), (5, 6)),
        ((4, 6), (4, 7), (4, 8)),
        ((4, 5), (4, 6), (4, 7)),
        ((6, 4), (6, 5), (6, 6))],
        ((0, 2), (0, 3), (0, 4)): [((0, 1), (0, 2), (0, 3)),
        ((1, 3), (1, 4), (1, 5)),
        ((1, 2), (1, 3), (1, 4))],
        ((2, 3), (1, 3), (0, 3)): [((2, 4), (1, 4), (0, 4)),
        ((2, 2), (1, 2), (0, 2)),
        ((3, 4), (2, 4), (1, 4)),
        ((3, 3), (2, 3), (1, 3))],
        ((5, 1), (5, 2), (5, 3)): [((5, 2), (5, 3), (5, 4)),
        ((5, 0), (5, 1), (5, 2)),
        ((4, 2), (4, 3), (4, 4)),
        ((4, 1), (4, 2), (4, 3)),
        ((6, 1), (6, 2), (6, 3)),
        ((6, 0), (6, 1), (6, 2))],
        ((7, 0), (7, 1), (7, 2)): [((7, 1), (7, 2), (7, 3)),
        ((6, 1), (6, 2), (6, 3)),
        ((6, 0), (6, 1), (6, 2)),
        ((8, 0), (8, 1), (8, 2))],
        ((5, 6), (4, 7), (3, 7)): [((5, 5), (4, 6), (3, 6)),
        ((4, 6), (3, 6), (2, 6)),
        ((6, 6), (5, 7), (4, 8)),
        ((6, 5), (5, 6), (4, 7))],
        ((4, 3), (5, 3), (6, 3)): [((4, 4), (5, 4), (6, 4)),
        ((4, 2), (5, 2), (6, 2)),
        ((3, 3), (4, 4), (5, 4)),
        ((3, 2), (4, 3), (5, 3)),
        ((5, 3), (6, 3), (7, 3)),
        ((5, 2), (6, 2), (7, 2))],
        ((2, 4), (2, 5), (2, 6)): [((2, 3), (2, 4), (2, 5)),
        ((1, 3), (1, 4), (1, 5)),
        ((3, 5), (3, 6), (3, 7)),
        ((3, 4), (3, 5), (3, 6))],
        ((5, 2), (4, 3), (3, 3)): [((5, 3), (4, 4), (3, 4)),
        ((5, 1), (4, 2), (3, 2)),
        ((4, 3), (3, 3), (2, 3)),
        ((4, 2), (3, 2), (2, 2)),
        ((6, 2), (5, 3), (4, 4)),
        ((6, 1), (5, 2), (4, 3))],
        ((3, 4), (4, 5), (5, 5)): [((3, 5), (4, 6), (5, 6)),
        ((3, 3), (4, 4), (5, 4)),
        ((2, 4), (3, 5), (4, 6)),
        ((2, 3), (3, 4), (4, 5)),
        ((4, 5), (5, 5), (6, 5)),
        ((4, 4), (5, 4), (6, 4))],
        ((8, 1), (7, 2), (6, 3)): [((8, 2), (7, 3), (6, 4)),
        ((8, 0), (7, 1), (6, 2)),
        ((7, 2), (6, 3), (5, 4)),
        ((7, 1), (6, 2), (5, 3))],
        ((5, 2), (5, 3), (5, 4)): [((5, 3), (5, 4), (5, 5)),
        ((5, 1), (5, 2), (5, 3)),
        ((4, 3), (4, 4), (4, 5)),
        ((4, 2), (4, 3), (4, 4)),
        ((6, 2), (6, 3), (6, 4)),
        ((6, 1), (6, 2), (6, 3))],
        ((3, 4), (2, 4), (1, 4)): [((3, 5), (2, 5), (1, 5)),
        ((3, 3), (2, 3), (1, 3)),
        ((2, 4), (1, 4), (0, 4)),
        ((2, 3), (1, 3), (0, 3)),
        ((4, 5), (3, 5), (2, 5)),
        ((4, 4), (3, 4), (2, 4))],
        ((8, 0), (8, 1), (8, 2)): [((8, 1), (8, 2), (8, 3)),
        ((7, 1), (7, 2), (7, 3)),
        ((7, 0), (7, 1), (7, 2))],
        ((7, 3), (6, 4), (5, 5)): [((7, 4), (6, 5), (5, 6)),
        ((7, 2), (6, 3), (5, 4)),
        ((6, 4), (5, 5), (4, 6)),
        ((6, 3), (5, 4), (4, 5)),
        ((8, 3), (7, 4), (6, 5)),
        ((8, 2), (7, 3), (6, 4))],
        ((4, 2), (4, 3), (4, 4)): [((4, 3), (4, 4), (4, 5)),
        ((4, 1), (4, 2), (4, 3)),
        ((3, 2), (3, 3), (3, 4)),
        ((3, 1), (3, 2), (3, 3)),
        ((5, 2), (5, 3), (5, 4)),
        ((5, 1), (5, 2), (5, 3))],
        ((0, 0), (0, 1), (0, 2)): [((0, 1), (0, 2), (0, 3)),
        ((1, 1), (1, 2), (1, 3)),
        ((1, 0), (1, 1), (1, 2))],
        ((5, 2), (6, 2), (7, 2)): [((5, 3), (6, 3), (7, 3)),
        ((5, 1), (6, 1), (7, 1)),
        ((4, 3), (5, 3), (6, 3)),
        ((4, 2), (5, 2), (6, 2)),
        ((6, 2), (7, 2), (8, 2)),
        ((6, 1), (7, 1), (8, 1))],
        ((2, 4), (1, 4), (0, 4)): [((2, 3), (1, 3), (0, 3)),
        ((3, 5), (2, 5), (1, 5)),
        ((3, 4), (2, 4), (1, 4))],
        ((3, 3), (2, 3), (1, 3)): [((3, 4), (2, 4), (1, 4)),
        ((3, 2), (2, 2), (1, 2)),
        ((2, 3), (1, 3), (0, 3)),
        ((2, 2), (1, 2), (0, 2)),
        ((4, 4), (3, 4), (2, 4)),
        ((4, 3), (3, 3), (2, 3))],
        ((5, 3), (4, 4), (3, 4)): [((5, 4), (4, 5), (3, 5)),
        ((5, 2), (4, 3), (3, 3)),
        ((4, 4), (3, 4), (2, 4)),
        ((4, 3), (3, 3), (2, 3)),
        ((6, 3), (5, 4), (4, 5)),
        ((6, 2), (5, 3), (4, 4))],
        ((5, 0), (6, 0), (7, 0)): [((5, 1), (6, 1), (7, 1)),
        ((4, 1), (5, 1), (6, 1)),
        ((4, 0), (5, 0), (6, 0)),
        ((6, 0), (7, 0), (8, 0))],
        ((5, 5), (4, 6), (3, 6)): [((5, 6), (4, 7), (3, 7)),
        ((5, 4), (4, 5), (3, 5)),
        ((4, 6), (3, 6), (2, 6)),
        ((4, 5), (3, 5), (2, 5)),
        ((6, 5), (5, 6), (4, 7)),
        ((6, 4), (5, 5), (4, 6))],
        ((5, 0), (4, 1), (3, 1)): [((5, 1), (4, 2), (3, 2)),
        ((4, 1), (3, 1), (2, 1)),
        ((4, 0), (3, 0), (2, 0)),
        ((6, 0), (5, 1), (4, 2))],
        ((4, 4), (4, 5), (4, 6)): [((4, 5), (4, 6), (4, 7)),
        ((4, 3), (4, 4), (4, 5)),
        ((3, 4), (3, 5), (3, 6)),
        ((3, 3), (3, 4), (3, 5)),
        ((5, 4), (5, 5), (5, 6)),
        ((5, 3), (5, 4), (5, 5))],
        ((2, 0), (1, 0), (0, 0)): [((2, 1), (1, 1), (0, 1)),
        ((3, 1), (2, 1), (1, 1)),
        ((3, 0), (2, 0), (1, 0))],
        ((8, 3), (7, 4), (6, 5)): [((8, 4), (7, 5), (6, 6)),
        ((8, 2), (7, 3), (6, 4)),
        ((7, 4), (6, 5), (5, 6)),
        ((7, 3), (6, 4), (5, 5))],
        ((6, 3), (7, 3), (8, 3)): [((6, 4), (7, 4), (8, 4)),
        ((6, 2), (7, 2), (8, 2)),
        ((5, 4), (6, 4), (7, 4)),
        ((5, 3), (6, 3), (7, 3))],
        ((6, 2), (5, 3), (4, 4)): [((6, 3), (5, 4), (4, 5)),
        ((6, 1), (5, 2), (4, 3)),
        ((5, 3), (4, 4), (3, 4)),
        ((5, 2), (4, 3), (3, 3)),
        ((7, 2), (6, 3), (5, 4)),
        ((7, 1), (6, 2), (5, 3))],
        ((5, 0), (5, 1), (5, 2)): [((5, 1), (5, 2), (5, 3)),
        ((4, 1), (4, 2), (4, 3)),
        ((4, 0), (4, 1), (4, 2)),
        ((6, 0), (6, 1), (6, 2))],
        ((2, 2), (2, 3), (2, 4)): [((2, 3), (2, 4), (2, 5)),
        ((2, 1), (2, 2), (2, 3)),
        ((1, 2), (1, 3), (1, 4)),
        ((1, 1), (1, 2), (1, 3)),
        ((3, 3), (3, 4), (3, 5)),
        ((3, 2), (3, 3), (3, 4))],
        ((7, 5), (6, 6), (5, 7)): [((7, 4), (6, 5), (5, 6)),
        ((6, 6), (5, 7), (4, 8)),
        ((6, 5), (5, 6), (4, 7)),
        ((8, 4), (7, 5), (6, 6))],
        ((4, 5), (5, 5), (6, 5)): [((4, 6), (5, 6), (6, 6)),
        ((4, 4), (5, 4), (6, 4)),
        ((3, 5), (4, 6), (5, 6)),
        ((3, 4), (4, 5), (5, 5)),
        ((5, 5), (6, 5), (7, 5)),
        ((5, 4), (6, 4), (7, 4))],
        ((3, 3), (4, 4), (5, 4)): [((3, 4), (4, 5), (5, 5)),
        ((3, 2), (4, 3), (5, 3)),
        ((2, 3), (3, 4), (4, 5)),
        ((2, 2), (3, 3), (4, 4)),
        ((4, 4), (5, 4), (6, 4)),
        ((4, 3), (5, 3), (6, 3))],
        ((3, 3), (3, 4), (3, 5)): [((3, 4), (3, 5), (3, 6)),
        ((3, 2), (3, 3), (3, 4)),
        ((2, 3), (2, 4), (2, 5)),
        ((2, 2), (2, 3), (2, 4)),
        ((4, 4), (4, 5), (4, 6)),
        ((4, 3), (4, 4), (4, 5))],
        ((2, 0), (2, 1), (2, 2)): [((2, 1), (2, 2), (2, 3)),
        ((1, 0), (1, 1), (1, 2)),
        ((3, 1), (3, 2), (3, 3)),
        ((3, 0), (3, 1), (3, 2))],
        ((7, 1), (7, 2), (7, 3)): [((7, 2), (7, 3), (7, 4)),
        ((7, 0), (7, 1), (7, 2)),
        ((6, 2), (6, 3), (6, 4)),
        ((6, 1), (6, 2), (6, 3)),
        ((8, 1), (8, 2), (8, 3)),
        ((8, 0), (8, 1), (8, 2))],
        ((3, 5), (3, 6), (3, 7)): [((3, 4), (3, 5), (3, 6)),
        ((2, 4), (2, 5), (2, 6)),
        ((4, 6), (4, 7), (4, 8)),
        ((4, 5), (4, 6), (4, 7))],
        ((5, 1), (4, 2), (3, 2)): [((5, 2), (4, 3), (3, 3)),
        ((5, 0), (4, 1), (3, 1)),
        ((4, 2), (3, 2), (2, 2)),
        ((4, 1), (3, 1), (2, 1)),
        ((6, 1), (5, 2), (4, 3)),
        ((6, 0), (5, 1), (4, 2))],
        ((3, 0), (4, 1), (5, 1)): [((3, 1), (4, 2), (5, 2)),
        ((2, 0), (3, 1), (4, 2)),
        ((4, 1), (5, 1), (6, 1)),
        ((4, 0), (5, 0), (6, 0))],
        ((2, 6), (3, 7), (4, 8)): [((2, 5), (3, 6), (4, 7)),
        ((1, 5), (2, 6), (3, 7)),
        ((3, 6), (4, 7), (5, 7))],
        ((5, 5), (6, 5), (7, 5)): [((5, 4), (6, 4), (7, 4)),
        ((4, 6), (5, 6), (6, 6)),
        ((4, 5), (5, 5), (6, 5)),
        ((6, 4), (7, 4), (8, 4))],
        ((3, 0), (3, 1), (3, 2)): [((3, 1), (3, 2), (3, 3)),
        ((2, 0), (2, 1), (2, 2)),
        ((4, 1), (4, 2), (4, 3)),
        ((4, 0), (4, 1), (4, 2))],
        ((3, 1), (4, 2), (5, 2)): [((3, 2), (4, 3), (5, 3)),
        ((3, 0), (4, 1), (5, 1)),
        ((2, 1), (3, 2), (4, 3)),
        ((2, 0), (3, 1), (4, 2)),
        ((4, 2), (5, 2), (6, 2)),
        ((4, 1), (5, 1), (6, 1))],
        ((3, 2), (4, 3), (5, 3)): [((3, 3), (4, 4), (5, 4)),
        ((3, 1), (4, 2), (5, 2)),
        ((2, 2), (3, 3), (4, 4)),
        ((2, 1), (3, 2), (4, 3)),
        ((4, 3), (5, 3), (6, 3)),
        ((4, 2), (5, 2), (6, 2))],
        ((2, 0), (3, 1), (4, 2)): [((2, 1), (3, 2), (4, 3)),
        ((1, 0), (2, 1), (3, 2)),
        ((3, 1), (4, 2), (5, 2)),
        ((3, 0), (4, 1), (5, 1))],
        ((6, 1), (7, 1), (8, 1)): [((6, 2), (7, 2), (8, 2)),
        ((6, 0), (7, 0), (8, 0)),
        ((5, 2), (6, 2), (7, 2)),
        ((5, 1), (6, 1), (7, 1))],
        ((5, 1), (6, 1), (7, 1)): [((5, 2), (6, 2), (7, 2)),
        ((5, 0), (6, 0), (7, 0)),
        ((4, 2), (5, 2), (6, 2)),
        ((4, 1), (5, 1), (6, 1)),
        ((6, 1), (7, 1), (8, 1)),
        ((6, 0), (7, 0), (8, 0))],
        ((2, 3), (2, 4), (2, 5)): [((2, 4), (2, 5), (2, 6)),
        ((2, 2), (2, 3), (2, 4)),
        ((1, 3), (1, 4), (1, 5)),
        ((1, 2), (1, 3), (1, 4)),
        ((3, 4), (3, 5), (3, 6)),
        ((3, 3), (3, 4), (3, 5))],
        ((4, 6), (3, 6), (2, 6)): [((4, 5), (3, 5), (2, 5)),
        ((3, 5), (2, 5), (1, 5)),
        ((5, 6), (4, 7), (3, 7)),
        ((5, 5), (4, 6), (3, 6))],
        ((5, 4), (4, 5), (3, 5)): [((5, 5), (4, 6), (3, 6)),
        ((5, 3), (4, 4), (3, 4)),
        ((4, 5), (3, 5), (2, 5)),
        ((4, 4), (3, 4), (2, 4)),
        ((6, 4), (5, 5), (4, 6)),
        ((6, 3), (5, 4), (4, 5))],
        ((6, 4), (5, 5), (4, 6)): [((6, 5), (5, 6), (4, 7)),
        ((6, 3), (5, 4), (4, 5)),
        ((5, 5), (4, 6), (3, 6)),
        ((5, 4), (4, 5), (3, 5)),
        ((7, 4), (6, 5), (5, 6)),
        ((7, 3), (6, 4), (5, 5))],
        ((3, 2), (3, 3), (3, 4)): [((3, 3), (3, 4), (3, 5)),
        ((3, 1), (3, 2), (3, 3)),
        ((2, 2), (2, 3), (2, 4)),
        ((2, 1), (2, 2), (2, 3)),
        ((4, 3), (4, 4), (4, 5)),
        ((4, 2), (4, 3), (4, 4))],
        ((4, 5), (4, 6), (4, 7)): [((4, 6), (4, 7), (4, 8)),
        ((4, 4), (4, 5), (4, 6)),
        ((3, 5), (3, 6), (3, 7)),
        ((3, 4), (3, 5), (3, 6)),
        ((5, 5), (5, 6), (5, 7)),
        ((5, 4), (5, 5), (5, 6))],
        ((3, 4), (3, 5), (3, 6)): [((3, 5), (3, 6), (3, 7)),
        ((3, 3), (3, 4), (3, 5)),
        ((2, 4), (2, 5), (2, 6)),
        ((2, 3), (2, 4), (2, 5)),
        ((4, 5), (4, 6), (4, 7)),
        ((4, 4), (4, 5), (4, 6))],
        ((0, 4), (1, 5), (2, 6)): [((0, 3), (1, 4), (2, 5)),
        ((1, 5), (2, 6), (3, 7)),
        ((1, 4), (2, 5), (3, 6))],
        ((6, 1), (6, 2), (6, 3)): [((6, 2), (6, 3), (6, 4)),
        ((6, 0), (6, 1), (6, 2)),
        ((5, 2), (5, 3), (5, 4)),
        ((5, 1), (5, 2), (5, 3)),
        ((7, 1), (7, 2), (7, 3)),
        ((7, 0), (7, 1), (7, 2))],
        ((5, 4), (6, 4), (7, 4)): [((5, 5), (6, 5), (7, 5)),
        ((5, 3), (6, 3), (7, 3)),
        ((4, 5), (5, 5), (6, 5)),
        ((4, 4), (5, 4), (6, 4)),
        ((6, 4), (7, 4), (8, 4)),
        ((6, 3), (7, 3), (8, 3))],
        ((1, 0), (1, 1), (1, 2)): [((1, 1), (1, 2), (1, 3)),
        ((0, 0), (0, 1), (0, 2)),
        ((2, 1), (2, 2), (2, 3)),
        ((2, 0), (2, 1), (2, 2))],
        ((2, 2), (1, 2), (0, 2)): [((2, 3), (1, 3), (0, 3)),
        ((2, 1), (1, 1), (0, 1)),
        ((3, 3), (2, 3), (1, 3)),
        ((3, 2), (2, 2), (1, 2))],
        ((4, 1), (3, 1), (2, 1)): [((4, 2), (3, 2), (2, 2)),
        ((4, 0), (3, 0), (2, 0)),
        ((3, 1), (2, 1), (1, 1)),
        ((3, 0), (2, 0), (1, 0)),
        ((5, 1), (4, 2), (3, 2)),
        ((5, 0), (4, 1), (3, 1))],
        ((3, 5), (2, 5), (1, 5)): [((3, 4), (2, 4), (1, 4)),
        ((2, 4), (1, 4), (0, 4)),
        ((4, 6), (3, 6), (2, 6)),
        ((4, 5), (3, 5), (2, 5))]}


    """
    param color
    return the opsite color from the one which it is his turn
    """
    @njit
    def opsite(color):
        if color == 2:
            return 3
        else:
            return 2
    
    """
    param key
    param position on the board
    return if the position is on the key
    """
    def on_key(key,pos):
        for i in key:
            if np.array_equal(i,pos):
                return True
        return False

    '''
    param positions on board
    param the color of the pieces
    return if the color is in the positions
    '''
    def on_board(key,color):
        for i in key:
            if (self.board)[i[0]][i[1]] != color:
                return False
        return True

    """
    param key
    param move
    return the direction of the move
    """
    def get_dir(key,move):
        return np.array((move[0]-key[0],move[1]-key[1]),dtype='i1')

    """
    param key
    param move
    return if the move has sideways
    """
    def move_type(key,move):
        for i in key:
            for j in move:
                if np.array_equal(i,j):
                    return False
        return True

    """
    param current position
    param the move
    return if the move is legal
    """
    def legal_move(key,move,color):
        key = np.array(key, dtype='i1')
        move = np.array(move, dtype='i1')

        if move_type(key,move):
            for pos in move:
                if (self.board)[pos[0]][pos[1]] != 1:
                    return False
            return True
        
        else:
            dir = get_dir(key,move)
            cur_pos = np.copy(move[0])
            #warning cur_pos can go out of the board
            while on_key(key,cur_pos):
                cur_pos[0] += dir[0]
                cur_pos[1] += dir[1]
            count = 0
            while (self.board)[cur_pos[0]][cur_pos[1]] == opsite(color):
                count += 1
                cur_pos[0] += dir[0]
                cur_pos[1] += dir[1]
            return count < len(key) and (self.board)[cur_pos[0]][cur_pos[1]] != color

    """
    param potential moves each representing a unique set
    param the color
    return a dictionary with all the legal moves

    idea of the code
    for each key in check if it's on the board, and if yes add it to res.
    for each key on the board iterate over the possible moves, and check if they are legal.
    """
    def legal_moves(self,color):
        for key in self.moves:
            if on_board(key,color):
                to_add = list({})##
                for move in (self.moves)[key]:
                    if legal_move(key,move,color):##
                        to_add.append(move)
                if color == 2:
                    self.moves_white[key] = np.array(to_add, dtype= 'i1')
                else:
                    self.moves_black[key] = np.array(to_add, dtype= 'i1')