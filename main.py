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
        self.h = 0 # heuristic value of current board.
        self.cost = 0 # depth of current board.
        self._parent = None # parent board of current board, probably useful? Check after finish Puzzle class.

    def print(self):
        """
        Prints out the current board.
        """
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == 0:
                    print(" ")
                else:
                    print(self.board[i][j])
            print("\n")

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
                # if there is a difference btw current board and goal board, return False and break.
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

    def getLegalMoves(self, curr_board):
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
    
    def costFunction(self):
        """
        Calculates the cost of path g(n) from the initial board to the current board.
        Notice that f(n) = g(n) + h(n).
        :return (int) cost - the number of actions already taken.
        """
        legal_moves = self.getLegalMoves()
        ava_blank = self.getIndex(0)
        self.cost += 1
        return self.cost

    def heuristicFunction(self):
        """
        Implements a heuristic function h(n).
        Notice that f(n) = g(n) + h(n).
        :return (int) count - the number of different slots between current board and goal.
        """
        board_to_check = [0,0,0,0,0,0,0,0,0]
        for i in range(0,3):
            for j in range(0,3):
                board_to_check[i+j] = self.board[i][j]
        board_is_goal = [0,1,2,3,4,5,6,7,8]
        count = 0
        for i in range(len(board_to_check)):
            if board_to_check[i] != board_is_goal[i]:
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
                    # j = PathNode(i[0], i[1], i[2], next, next.costsum + i[2], heuristic(i[0], problem))
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




