import abaloneAI.board as br

number_of_games = 1000
max_turns = 150

for i in range(number_of_games):
    #creates a new board
    board = br.board()

    isFinished = False
    color = 2

    #the game 
    for j in range(max_turns):
        if board.get_whites() == 0 or board.get_blacks() == 0:
            break

        board.legal_moves(color)

        choose(board,color,)

        color = opposite(color)

def turn(board,color,):
    pass

def choose(board,color,key,move):
    board.move(color,key,move)


def opposite(color):
        """
        param color
        return the opposite color from the one which it is his turn
        """
        if color == 2:
            return 3
        else:
            return 2
    