# ***********************************************************************************************************
# 8 Puzzle Problem
# Tiles are numbered, 1 thru 8 for the 8-puzzle, so that each tile can be uniquely identified. The aim of
# the puzzle is to achieve a given configuration of tiles from a given (different) configuration by sliding
# the individual tiles around the grid as described above.
# (Reference: Google)
# ***********************************************************************************************************
# Solver: This python program is an AI solver of a 8 Puzzle Game using A* search algorithm,
# written by YM Li, in Fall 2018.
# ***********************************************************************************************************

##
class Puzzle:
    def __init__(self, board):
        self.board = board # an array input representing the board.
        self.h = 0 # heuristic value of current board.
        self.depth = 0 # depth of current board.
        # self._parent = None # parent board of current board, probably useful? Check after finish Puzzle class.

    ## Checks the goal states.
    def isGoal(self):
        if self.board == [1,2,3,4,5,6,7,8,0] or self.board == [0,1,2,3,4,5,6,7,8]:
            return True
        return False

    ## Prints out the current board.
    def print(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.board[i+j])
            print("\n")

    ## Shuffles the current board.
    def shuffle(self):
        return None

##
class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    ## Applies manhattan distance as heuristic function.
    def manhattanDistance(self):
        return None

    def heuristicFunction(self):
        return None

    ## Applies A* search.
    def aStarSearch(self):
        return None



