from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lines = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        cubes = [[] for _ in range(9)]
        for index, line in enumerate(board):  # index=0, line = [5,3,,,...]
            for column_index, num in enumerate(line):  # index = 0, num=5
                if not num.isdigit():
                    continue

                lines[index].append(num)
                columns[column_index].append(num)

                if column_index < 3:
                    if index < 3:
                        cubes[0].append(num)
                    elif index < 6:
                        cubes[3].append(num)
                    else:
                        cubes[6].append(num)
                elif column_index < 6:
                    if index < 3:
                        cubes[1].append(num)
                    elif index < 6:
                        cubes[4].append(num)
                    else:
                        cubes[7].append(num)
                else:
                    if index < 3:
                        cubes[2].append(num)
                    elif index < 6:
                        cubes[5].append(num)
                    else:
                        cubes[8].append(num)

        for i in range(9):
            if (
                len(lines[i]) != len(set(lines[i]))
                or len(columns[i]) != len(set(columns[i]))
                or len(cubes[i]) != len(set(cubes[i]))
            ):
                return False

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert Solution().isValidSudoku(board) is True

board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
assert Solution().isValidSudoku(board) is False
