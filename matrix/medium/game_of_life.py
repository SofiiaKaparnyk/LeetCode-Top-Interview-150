from typing import List

"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by 
the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or 
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the 
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births 
and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = {}
        for row_i in range(len(board)):
            for col_i in range(len(board[row_i])):
                dead = alive = 0
                for i in range(-1, 2):
                    if row_i + i < 0 or row_i + i >= len(board):
                        continue
                    for j in range(-1, 2):
                        if col_i + j < 0 or col_i + j >= len(board[0]) or (i == 0 and j == 0):
                            continue
                        if board[row_i + i][col_i + j] == 0:
                            dead += 1
                        else:
                            alive += 1
                d[(row_i, col_i)] = {"dead": dead, "alive": alive}

        for row_col, value in d.items():
            if value["alive"] < 2 or value["alive"] > 3:
                board[row_col[0]][row_col[1]] = 0
            if value["alive"] == 3:
                board[row_col[0]][row_col[1]] = 1
        return board


assert Solution().gameOfLife(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]) == [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]
assert Solution().gameOfLife(board=[[1, 1], [1, 0]]) == [[1, 1], [1, 1]]
assert Solution().gameOfLife(board=[[1, 1], [1, 1]]) == [[1, 1], [1, 1]]
