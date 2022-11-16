"""
game board class
the class contains a counstractor and a ability to make moves
"""

# write and test game main
# write ai


import ast

import numpy as np


class GameBoard:
    """
    counstracts a new board
    """
    def __init__(self):
        # board
        # none = 0 empty = 1, white = 2, black = 3
        self.board = np.array([
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
        self.pos1 = np.load('large_variables/pos1.npy')
        self.pos2 = np.load('large_variables/pos2.npy')
        self.pos3 = np.load('large_variables/pos3.npy')

        # possible moves
        self.moves_black = {}
        self.moves_white = {}

        #check
        with open('large_variables/moves.txt', 'r',encoding='txt') as f:
            dic = f.read()

        self.moves = ast.literal_eval(dic)

    def row_length(self,row):
        """
        param row
        return row length
        """
        if(row<5):
            return row+5
        return 13-row

    def to_string(self):
        """
        prints the board
        """
        board = self.board.tolist()
        for row in range(9):
            for pos in range(9):
                if board[row][pos] == 1:
                    board[row][pos] = '.'
                elif board[row][pos] == 2:
                    board[row][pos] = 'O'
                elif board[row][pos] == 3:
                    board[row][pos] = 'X'
                else:
                    board[row][pos] = ''

        for row in range(9):
            length = 15-self.row_length(row)
            print(" "*length +' '.join(board[row]))

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
            return np.array((self.r(t[0])))
        elif len(t) == 2:
            return np.array((self.r(t[0]),self.r(t[1])))
        else:
            return np.array((self.r(t[0]),self.r(t[1]),self.r(t[2])))

    def lt(self,t):
        if len(t) == 1:
            return np.array((self.l(t[0])))
        elif len(t) == 2:
            return np.array((self.l(t[0]),self.l(t[1])))
        else:
            return np.array((self.l(t[0]),self.l(t[1]),self.l(t[2])))

    def rut(self,t):
        if len(t) == 1:
            return np.array((self.ru(t[0])))
        elif len(t) == 2:
            return np.array((self.ru(t[0]),self.ru(t[1])))
        else:
            return np.array((self.ru(t[0]),self.ru(t[1]),self.ru(t[2])))

    def lut(self,t):
        if len(t) == 1:
            return np.array((self.lu(t[0])))
        elif len(t) == 2:
            return np.array((self.lu(t[0]),self.lu(t[1])))
        else:
            return np.array((self.lu(t[0]),self.lu(t[1]),self.lu(t[2])))

    def rdt(self,t):
        if len(t) == 1:
            return np.array((self.rd(t[0])))
        elif len(t) == 2:
            return np.array((self.rd(t[0]),self.rd(t[1])))
        else:
            return np.array((self.rd(t[0]),self.rd(t[1]),self.rd(t[2])))

    def ldt(self,t):
        if len(t) == 1:
            return np.array((self.ld(t[0])))
        elif len(t) == 2:
            return np.array((self.ld(t[0]),self.ld(t[1])))
        else:
            return np.array((self.ld(t[0]),self.ld(t[1]),self.ld(t[2])))

    def get_dir(self,key,move):
        """
        param key
        param move
        return the direction of movement
        """
        if np.array_equal(self.rt(key),move):
            return 'r'
        elif np.array_equal(self.lt(key),move):
            return 'l'
        elif np.array_equal(self.rut(key),move):
            return 'ru'
        elif np.array_equal(self.lut(key),move):
            return 'lu'
        elif np.array_equal(self.rdt(key),move):
            return 'rd'
        elif np.array_equal(self.ldt(key),move):
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
            res = self.r(cur_pos)
        elif dir == 'l':
            res = self.l(cur_pos)
        elif dir == 'ru':
            res = self.ru(cur_pos)
        elif dir == 'lu':
            res = self.lu(cur_pos)
        elif dir == 'rd':
            res = self.rd(cur_pos)
        elif dir == 'ld':
            res = self.ld(cur_pos)
        else:
            raise ValueError("IllegalDirection")

        if not((res[0] <= 8 and res[0] >= 0) and (res[1] <= 8 and res[1] >= 0)):
            raise ValueError("IndexOutOfBoard")

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

    @classmethod
    def opposite(cls,color):
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
        if self.move_type(key,move):
            for pos in move:
                if (self.board)[pos[0]][pos[1]] != 1:
                    return False
            return True

        else:
            dir = self.get_dir(key,move)
            cur_pos = np.copy(move[0])

            while self.in_key(key,cur_pos):
                try:
                    cur_pos = self.advance(cur_pos,dir)
                except ValueError:
                    break
            count = 0

            while (self.board)[cur_pos[0]][cur_pos[1]] == self.opposite(color):
                count += 1
                try:
                    cur_pos = self.advance(cur_pos,dir)
                except ValueError:
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
            if self.on_board(key,color):

                to_add = list({})

                for move in (self.moves)[key]:
                    if self.legal_move(key,move,color):
                        to_add.append(move)

                #checks where to add the moves
                if len(to_add) != 0:
                    if color == 2:
                        (self.moves_white)[key] = np.array(to_add, dtype= 'i1')
                    else:
                        (self.moves_black)[key] = np.array(to_add, dtype= 'i1')

    def first(self,key,move):
        """
        param key
        param move
        returns the position in key which isn't present in move
        """
        if not self.in_key(move,key[0]):
            return np.array(key[0],dtype='i1')
        return np.array(key[len(key)-1],dtype='i1')

    def move_(self,color,key,move):
        """
        param color
        param key
        param move
        makes the move on the board
        """
        if self.move_type(key,move):
            for pos in key:
                (self.board)[pos[0]][pos[1]] = 0
            for pos in move:
                (self.board)[pos[0]][pos[1]] = color

        else:
            dir = self.get_dir(key,move)
            cur_pos = self.first(key,move)
            last_color = (self.board)[cur_pos[0]][cur_pos[1]]

            (self.board)[cur_pos[0]][cur_pos[1]] = 1

            while last_color != 1 and last_color != 0:
                try:
                    cur_pos = self.advance(cur_pos,dir)
                    cur_color = (self.board)[cur_pos[0]][cur_pos[1]]
                    (self.board)[cur_pos[0]][cur_pos[1]] = last_color
                    last_color = cur_color
                except ValueError:
                    break
