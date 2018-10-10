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

import heapq, random


class Puzzle:
    """

    """
    def __init__(self, board):
        self.board = board # a 2D array input representing the board.
        self.heuristic_value = 0 # heuristic value of current board.
        self.cost = 0 # depth of current board.
        self.parent = None
        self.next = None

    def print(self):
        """
        Prints out the current board.
        """
        if self.cost == 0:
            print("Welcome! Here is the initial board.\nIf you wanna test other boards, dive into the code!")
        else:
            print("This is step "+str(self.cost)+" of the path." )

        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == 0:
                    print(" ", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print("\n", end="")

    def isGoal(self):
        """
        Checks the goal states.
        The specific goal state is:
                          1 2
                        3 4 5
                        6 7 8
                                    for this game.
        :return (bool) True - if current board match the goal board,
                 (bool) False - otherwise.
        """
        goal_board = [[0,1,2], [3,4,5], [6,7,8]]
        for i in range(0,3):
            for j in range(0,3):
                # if there is a difference btw current board and goal board, return False.
                if self.board[i][j] != goal_board[i][j]:
                    return False
        # otherwise, return True.
        return True

    def getIndex(self, num):
        """
        Get the index to move of a specific number in current board.
        :return: (int tuple) i,j - index of the number waiting for check,
                  (int tuple) 999,999 - if there is no such a number (ERROR msg).
        """
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == num:
                    return (i,j)
        return (999,999)

    def getLegalMoves(self):
        """
        Get the available items to move according to current blank.
        :return: (tuple array) moves - array of tuples representing indices of legal moves.
        """
        moves = []
        legal_move = self.getIndex(0) # NOTICE: if there is a legal move, it should be 0.

        if legal_move == (0,0):
            moves.append((0,1))
            moves.append((1,0))
        elif legal_move == (0,1):
            moves.append((0,0))
            moves.append((0,2))
            moves.append((1,1))
        elif legal_move == (0,2):
            moves.append((0,1))
            moves.append((1,2))
        elif legal_move == (1,0):
            moves.append((0,0))
            moves.append((1,1))
            moves.append((2,0))
        elif legal_move == (1,1):
            moves.append((0,1))
            moves.append((1,0))
            moves.append((1,2))
            moves.append((2,1))
        elif legal_move == (1,2):
            moves.append((0,2))
            moves.append((1,1))
            moves.append((2,2))
        elif legal_move == (2,0):
            moves.append((1,0))
            moves.append((2,1))
        elif legal_move == (2,1):
            moves.append((1,1))
            moves.append((2,0))
            moves.append((2,2))
        else: #legal_move = (2,2)
            moves.append((1,2))
            moves.append((2,1))

        return moves

    def swapBoard(self, blank_index, legal_move_index):
        temp = self.board[legal_move_index[0]][legal_move_index[1]]
        # print("temp: "+ str(temp))
        self.board[legal_move_index[0]][legal_move_index[1]] = 0
        self.board[blank_index[0]][blank_index[1]] = temp
        #print("***")
        #self.print()

    def copyBoard(self):
        copy_board = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(0,3):
            for j in range(0,3):
                copy_board[i][j] = self.board[i][j]
        return copy_board

    def getChildren(self):
        blank = self.getIndex(0)
        legals = self.getLegalMoves()
        children_num = len(legals)
        children_states = []
        for i in range(0, children_num):
            temp_board = self.copyBoard()
            temp = Puzzle(temp_board)
            temp.swapBoard(blank, legals[i])
            child_board = temp.copyBoard()
            child = Puzzle(child_board)
            child.parent = self
            child.cost += 1
            # print(child.cost)
            children_states.append(child)

        return children_states

    def heuristicFunction(self):
        """
        Implements a heuristic function h(n).
        Notice that f(n) = g(n) + h(n).
        :return (int) count - the number of different slots between current board and goal.
        """
        board = [0,0,0,0,0,0,0,0,0]
        children_states = self.getChildren()
        for i in range(0,3):
            for j in range(0,3):
                board[i+j] = board_to_check[i][j]
        board_is_goal = [0,1,2,3,4,5,6,7,8]
        count = 0
        for i in range(0,9):
            if board[i] != board_is_goal[i]:
                count += 1
        return count

    def AStarSearch(self):

        frontier = PriorityQueue()
        frontier.push((self.board, 0))
        explored = []
        tracks = []

        while not frontier.isEmpty():
            board_to_check = frontier.pop()
            if self.isGoal():
                while board_to_check.parent != None:
                    tracks.append(board_to_check)
                    board_to_check = board_to_check.parent
                    tracks.reverse()
                return tracks
            if board_to_check.board not in explored:
                explored.append(board_to_check.board)
                for board in self.getLegalMoves(board_to_check.board):
                    frontier.push((board, self.heuristicFunction(board)))
        return tracks


class PriorityQueue:
    """
      Applies the priority queue data structure.
      Items inserted is in the order of values related to them.
    """
    def __init__(self):
        self.priority_queue = []
        # self.count = 0

    def push(self, item):
        heapq.heappush(self.priority_queue, item)
        # self.count += 1

    def pop(self):
        return heapq.heappop(self.priority_queue)

    def isEmpty(self):
        return len(self.priority_queue) == 0

    def firstItem(self):
        return self.priority_queue[0]


def main():
    board = [[7,2,4],[5,0,6],[8,3,1]]
    puzzle = Puzzle(board)
    puzzle.print()
    # ****************************************
    #   Here are lines to test functions.
    # ****************************************
    #print(puzzle.getIndex(0))
    #for i in puzzle.getLegalMoves():
    #   print(puzzle.board[i[0]][i[1]])
    #childrens = puzzle.getChildren()
    #for i in range(0,4):
    #   childrens[i].print()
    # ****************************************

if __name__ == "__main__":
    main()

