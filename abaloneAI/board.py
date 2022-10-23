"""
Board class
"""

# TODO:
# resolve in ability of functions to call other functions inthe class
# write and test game main
# create intrface
# write ai

import numpy as np
import ast

class Board:
    """
    counstracts a new board
    """
    def __init__(self):
        # board
        # none = 0 empty = 1, white = 2, black = 3
        self.entries = np.array([
                [2, 2, 2, 2, 2, 0, 0, 0, 0],
                [2, 2, 2, 2, 2, 2, 0, 0, 0],
                [1, 1, 2, 2, 2, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 3, 3, 3, 1, 1, 0, 0],
                [3, 3, 3, 3, 3, 3, 0, 0, 0],
                [3, 3, 3, 3, 3, 0, 0, 0, 0],
            ],dtype='i1',)

        #num of turns made in the game and black and white
        self.num_of_turns = 0
        self.num_of_whites = 14
        self.num_of_blacks = 14

        #possible positions
        """
        with open('large_variables/pos1.txt', 'r') as f:
            pos1 = f.readlines()
        
        with open('large_variables/pos2.txt', 'r') as f:
            pos2 = f.readlines()

        with open('large_variables/pos3.txt', 'r') as f:
            pos3 = f.readlines()
        """
        self.pos1 = np.array(((7, 3),
        (4, 7),
        (1, 3),
        (4, 8),
        (3, 0),
        (0, 2),
        (5, 6),
        (6, 6),
        (8, 0),
        (2, 1),
        (6, 2),
        (3, 7),
        (2, 5),
        (0, 3),
        (5, 1),
        (7, 2),
        (4, 0),
        (1, 2),
        (3, 3),
        (5, 5),
        (8, 1),
        (4, 4),
        (6, 3),
        (1, 5),
        (3, 6),
        (2, 2),
        (0, 4),
        (5, 0),
        (4, 1),
        (1, 1),
        (6, 4),
        (3, 2),
        (0, 0),
        (2, 6),
        (5, 4),
        (8, 2),
        (7, 1),
        (4, 5),
        (5, 2),
        (6, 0),
        (1, 4),
        (7, 5),
        (2, 3),
        (4, 2),
        (1, 0),
        (6, 5),
        (3, 5),
        (0, 1),
        (5, 3),
        (8, 3),
        (7, 0),
        (4, 6),
        (6, 1),
        (3, 1),
        (5, 7),
        (7, 4),
        (2, 0),
        (4, 3),
        (3, 4),
        (2, 4),
        (8, 4)),dtype='i1')
        self.pos2 = np.array((((2, 6), (3, 6)),
        ((3, 3), (4, 4)),
        ((8, 3), (8, 4)),
        ((6, 4), (7, 4)),
        ((0, 2), (1, 2)),
        ((5, 6), (6, 5)),
        ((2, 3), (3, 4)),
        ((1, 1), (2, 1)),
        ((1, 5), (2, 5)),
        ((3, 1), (4, 2)),
        ((0, 2), (0, 3)),
        ((1, 4), (1, 5)),
        ((0, 4), (1, 5)),
        ((5, 6), (5, 7)),
        ((4, 5), (5, 5)),
        ((2, 2), (2, 3)),
        ((2, 5), (3, 5)),
        ((6, 5), (7, 4)),
        ((2, 3), (3, 3)),
        ((3, 3), (4, 3)),
        ((1, 2), (1, 3)),
        ((3, 2), (3, 3)),
        ((4, 8), (5, 7)),
        ((5, 4), (5, 5)),
        ((7, 0), (8, 0)),
        ((7, 2), (7, 3)),
        ((0, 1), (1, 2)),
        ((6, 1), (7, 0)),
        ((4, 4), (4, 5)),
        ((5, 3), (6, 2)),
        ((3, 7), (4, 8)),
        ((1, 4), (2, 5)),
        ((5, 6), (6, 6)),
        ((0, 0), (1, 0)),
        ((4, 6), (4, 7)),
        ((4, 7), (4, 8)),
        ((5, 4), (6, 3)),
        ((3, 4), (3, 5)),
        ((5, 2), (5, 3)),
        ((3, 4), (4, 4)),
        ((2, 5), (2, 6)),
        ((7, 2), (8, 1)),
        ((7, 4), (7, 5)),
        ((6, 0), (6, 1)),
        ((6, 4), (6, 5)),
        ((4, 6), (5, 6)),
        ((5, 2), (6, 2)),
        ((2, 1), (3, 1)),
        ((5, 1), (6, 1)),
        ((8, 1), (8, 2)),
        ((4, 4), (5, 3)),
        ((5, 2), (6, 1)),
        ((4, 7), (5, 7)),
        ((5, 3), (6, 3)),
        ((6, 3), (7, 3)),
        ((1, 0), (2, 0)),
        ((2, 1), (3, 2)),
        ((4, 1), (5, 1)),
        ((1, 2), (2, 2)),
        ((4, 6), (5, 5)),
        ((7, 4), (8, 4)),
        ((0, 3), (1, 3)),
        ((6, 1), (6, 2)),
        ((3, 4), (4, 5)),
        ((2, 3), (2, 4)),
        ((7, 1), (7, 2)),
        ((0, 1), (1, 1)),
        ((4, 5), (4, 6)),
        ((5, 5), (5, 6)),
        ((7, 3), (8, 3)),
        ((3, 6), (4, 7)),
        ((6, 1), (7, 1)),
        ((1, 0), (1, 1)),
        ((7, 4), (8, 3)),
        ((3, 3), (3, 4)),
        ((8, 2), (8, 3)),
        ((1, 3), (1, 4)),
        ((0, 0), (0, 1)),
        ((4, 4), (5, 4)),
        ((2, 0), (3, 1)),
        ((1, 3), (2, 3)),
        ((3, 7), (4, 7)),
        ((5, 5), (6, 4)),
        ((5, 1), (5, 2)),
        ((7, 5), (8, 4)),
        ((3, 6), (3, 7)),
        ((5, 0), (5, 1)),
        ((4, 7), (5, 6)),
        ((3, 5), (4, 6)),
        ((2, 2), (3, 2)),
        ((5, 4), (6, 4)),
        ((0, 2), (1, 3)),
        ((0, 0), (1, 1)),
        ((4, 3), (4, 4)),
        ((2, 0), (2, 1)),
        ((2, 4), (2, 5)),
        ((4, 2), (4, 3)),
        ((7, 1), (8, 1)),
        ((7, 0), (7, 1)),
        ((3, 5), (4, 5)),
        ((3, 0), (3, 1)),
        ((3, 6), (4, 6)),
        ((0, 4), (1, 4)),
        ((4, 3), (5, 2)),
        ((1, 4), (2, 4)),
        ((4, 2), (5, 2)),
        ((2, 4), (3, 4)),
        ((1, 0), (2, 1)),
        ((4, 5), (5, 4)),
        ((2, 4), (3, 5)),
        ((3, 1), (4, 1)),
        ((1, 1), (1, 2)),
        ((2, 0), (3, 0)),
        ((2, 2), (3, 3)),
        ((0, 3), (0, 4)),
        ((6, 2), (7, 1)),
        ((6, 3), (7, 2)),
        ((3, 0), (4, 0)),
        ((1, 5), (2, 6)),
        ((3, 2), (4, 3)),
        ((5, 3), (5, 4)),
        ((6, 2), (7, 2)),
        ((5, 5), (6, 5)),
        ((6, 2), (6, 3)),
        ((8, 0), (8, 1)),
        ((4, 2), (5, 1)),
        ((4, 0), (5, 0)),
        ((1, 3), (2, 4)),
        ((2, 1), (2, 2)),
        ((3, 1), (3, 2)),
        ((6, 0), (7, 0)),
        ((5, 1), (6, 0)),
        ((3, 0), (4, 1)),
        ((6, 5), (7, 5)),
        ((4, 3), (5, 3)),
        ((6, 5), (6, 6)),
        ((4, 0), (4, 1)),
        ((5, 7), (6, 6)),
        ((0, 3), (1, 4)),
        ((2, 6), (3, 7)),
        ((7, 3), (7, 4)),
        ((2, 5), (3, 6)),
        ((4, 1), (5, 0)),
        ((6, 3), (6, 4)),
        ((3, 5), (3, 6)),
        ((1, 1), (2, 2)),
        ((7, 1), (8, 0)),
        ((4, 1), (4, 2)),
        ((5, 0), (6, 0)),
        ((1, 2), (2, 3)),
        ((6, 6), (7, 5)),
        ((7, 3), (8, 2)),
        ((3, 2), (4, 2)),
        ((7, 2), (8, 2)),
        ((0, 1), (0, 2)),
        ((6, 4), (7, 3))), dtype = 'i1')
        self.pos3 = np.array((((0, 0), (0, 1), (0, 2)),
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
        ((8, 4), (7, 5), (6, 6))), dtype= 'i1')

        # possible moves
        self.moves_black = {}
        self.moves_white = {}

        with open('large_variables/moves.txt', 'r') as f:
            dic = f.read()
        
        self.moves = ast.literal_eval(dic)

    def get_whites(self):
        """
        returns the number of white pices respectivly
        """
        return self.num_of_whites

    def get_blacks(self):
        """
        returns the number of white or black pices respectivly
        """
        return self.num_of_blacks

    """
    param position
    return the entry advnced in a chosen direction

    the functions can advance in the right,left,right up,left up
    ,right down and left down all respectivly 
    """
    def r(self,entry):
        return np.array((entry[0],entry[1]+1),dtype='i1')

    def l(self,entry):
        res = (entry[0],entry[1]-1)
        return np.array(res,dtype='i1')

    def ru(self,entry):
        if(entry[0]<5):
            res = (entry[0]-1,entry[1])
        else:
            res = (entry[0]-1,entry[1]+1)
        return np.array(res,dtype='i1')

    def lu(self,entry):
        if(entry[0]<5):
            res = (entry[0]-1,entry[1]-1)
        else:
            res = (entry[0]-1,entry[1])
        return np.array(res,dtype='i1')

    def rd(self,entry):
        if(entry[0]<4):
            res = (entry[0]+1,entry[1]+1)
        else:
            res = (entry[0]+1,entry[1])
        return np.array(res,dtype='i1')

    def ld(self,entry):
        if(entry[0]<4):
            res = (entry[0]+1,entry[1])
        else:
            res = (entry[0]+1,entry[1]-1)
        return np.array(res,dtype='i1')
    
    """
    param group of positions
    return the group advnced in a chosen direction

    the functions can advance in the right,left,right up,left up
    ,right down and left down all respectivly 
    """
    def rt(self,t):
        if len(t) == 1:
            return np.array((r(t[0])))
        elif len(t) == 2:
            return np.array((r(t[0]),r(t[1])))
        else:
            return np.array((r(t[0]),r(t[1]),r(t[2])))

    def lt(self,t):
        if len(t) == 1:
            return np.array((l(t[0])))
        elif len(t) == 2:
            return np.array((l(t[0]),l(t[1])))
        else:
            return np.array((l(t[0]),l(t[1]),l(t[2])))

    def rut(self,t):
        if len(t) == 1:
            return np.array((ru(t[0])))
        elif len(t) == 2:
            return np.array((ru(t[0]),ru(t[1])))
        else:
            return np.array((ru(t[0]),ru(t[1]),ru(t[2])))

    def lut(self,t):
        if len(t) == 1:
            return np.array((lu(t[0])))
        elif len(t) == 2:
            return np.array((lu(t[0]),lu(t[1])))
        else:
            return np.array((lu(t[0]),lu(t[1]),lu(t[2])))

    def rdt(self,t):
        if len(t) == 1:
            return np.array((rd(t[0])))
        elif len(t) == 2:
            return np.array((rd(t[0]),rd(t[1])))
        else:
            return np.array((rd(t[0]),rd(t[1]),rd(t[2])))

    def ldt(self,t):
        if len(t) == 1:
            return np.array((ld(t[0])))
        elif len(t) == 2:
            return np.array((ld(t[0]),ld(t[1])))
        else:
            return np.array((ld(t[0]),ld(t[1]),ld(t[2])))

    def get_dir(self,key,move):
        """
        param key
        param move
        return the direction of movement
        """
        if np.array_equal(rt(key),move):
            return 'r'
        elif np.array_equal(lt(key),move):
            return 'l'
        elif np.array_equal(rut(key),move):
            return 'ru'
        elif np.array_equal(lut(key),move):
            return 'lu'
        elif np.array_equal(rdt(key),move):
            return 'rd'
        elif np.array_equal(ldt(key),move):
            return 'ld'
        else:
            return ''

    def advance(self,cur_pos,dir):
        """
        param current position
        param direction of movement
        return the current position advenced by the direction of movement
        """
        res = ''
        if dir == 'r':
            res = r(cur_pos)
        elif dir == 'l':
            res = l(cur_pos)
        elif dir == 'ru':
            res = ru(cur_pos)
        elif dir == 'lu':
            res = lu(cur_pos)
        elif dir == 'rd':
            res = rd(cur_pos)
        elif dir == 'ld':
            res = ld(cur_pos)
        else:
            raise Exception("IllegalDirection")
        
        if not((res[0] <= 8 and res[0] >= 0) and (res[1] <= 8 and res[1] >= 0)):
            raise Exception("IndexOutOfBoard")

        return res

    def move_type(self,key,move):
        """
        param key
        param move
        return if the move has sideways
        """
        for i in key:
            for j in move:
                if np.array_equal(i,j):
                    return False
        return True

    def opposite(self,color):
            """
            param color
            return the opposite color from the one which it is his turn
            """
            if color == 2:
                return 3
            else:
                return 2

    def in_key(self,key,pos):
            """
            param key
            param position on the board
            return if the position is in the key
            """
            for i in key:
                if np.array_equal(i,pos):
                    return True
            return False

    def on_board(self,key,color):
        """
        param positions on board
        param the color of the pieces
        return if the color is in the positions
        """
        for i in key:
            if (self.board)[i[0]][i[1]] != color:
                return False
        return True

    def legal_move(self,key,move,color):
        """
        param current position
        param the move
        return if the move is legal
        """
        if move_type(key,move):
            for pos in move:
                if (self.board)[pos[0]][pos[1]] != 1:
                    return False
            return True
        
        else:
            dir = get_dir(key,move)
            cur_pos = np.copy(move[0])
            
            while in_key(key,cur_pos):
                try:
                    cur_pos = advance(cur_pos,dir)
                except:
                    break
            count = 0

            while (self.board)[cur_pos[0]][cur_pos[1]] == opposite(color):
                count += 1
                try:
                    cur_pos = advance(cur_pos,dir)
                except:
                    break

            return count < len(key) and (self.board)[cur_pos[0]][cur_pos[1]] != color

    def legal_moves(self,color):
        """
        param potential moves each representing a unique set
        param the color
        return a dictionary with all the legal moves

        idea of the code
        for each key in check if it's on the board, and if yes add it to res.
        for each key on the board iterate over the possible moves, and check if they are legal.
        """
        #passes over every key
        for key in self.moves:
            if on_board(key,color):

                to_add = list({})

                for move in (self.moves)[key]:
                    if legal_move(key,move,color):
                        to_add.append(move)
                
                #checks where to add the moves
                if len(to_add) != 0:
                    if color == 2:
                        (self.moves_white)[key] = np.array(to_add, dtype= 'i1')
                    else:
                        (self.moves_black)[key] = np.array(to_add, dtype= 'i1')

    def first(self,key,move):
        for i in key:
            if not in_key(move,i):
                return i

    def move_(self,color,key,move):
        if move_type(key,move):
            for pos in key:
                (self.board)[pos[0]][pos[1]] = 0
            for pos in move:
                (self.board)[pos[0]][pos[1]] = color
        
        else:
            dir = get_dir(key,move)
            cur_pos = first(key,move)
            last_color = (self.board)[cur_pos[0]][cur_pos[1]]
            
            (self.board)[cur_pos[0]][cur_pos[1]] = 1
            
            while last_color != 1 and last_color != 0:
                try:
                    cur_pos = advance(cur_pos,dir)
                    cur_color = (self.board)[cur_pos[0]][cur_pos[1]]
                    (self.board)[cur_pos[0]][cur_pos[1]] = last_color
                    last_color = cur_color
                except:
                    break
