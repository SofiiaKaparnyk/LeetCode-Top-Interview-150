from typing import List

"""Given an m x n matrix, return all elements of the matrix in spiral order."""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new_ls = []
        rows = len(matrix)
        cols = len(matrix[0])

        row = col = 0
        first_row = 1
        first_col = 0
        last_row = rows - 1
        last_col = cols - 1
        if cols > 1:
            move = "r"
        else:
            move = "d"

        for _ in range(rows * cols):
            new_ls.append(matrix[row][col])
            if move == "r":
                col += 1
                if col == last_col:
                    move = "d"
                    last_col -= 1

            elif move == "l":
                col -= 1
                if col == first_col:
                    move = "u"
                    first_col += 1

            elif move == "d":
                row += 1
                if row == last_row:
                    move = "l"
                    last_row -= 1

            elif move == "u":
                row -= 1
                if row == first_row:
                    move = "r"
                    first_row += 1

        return new_ls


assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert Solution().spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
    1,
    2,
    3,
    4,
    8,
    12,
    11,
    10,
    9,
    5,
    6,
    7,
]
assert Solution().spiralOrder(matrix=[[3], [2]]) == [3, 2]
