from typing import List

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_indexes = []
        for row_i, row in enumerate(matrix):
            for col_i, num in enumerate(matrix[row_i]):
                if num == 0:
                    zero_indexes.append((row_i, col_i))

        for j in zero_indexes:
            for i in range(len(matrix)):
                matrix[i][j[1]] = 0

            for i in range(len(matrix[0])):
                matrix[j[0]][i] = 0
        return matrix


assert Solution().setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
assert Solution().setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]) == [
    [0, 0, 0, 0],
    [0, 4, 5, 0],
    [0, 3, 1, 0],
]
