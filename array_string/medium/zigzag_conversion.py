"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = 0
        step = 1
        array = [[] for _ in range(numRows)]
        for char in s:
            array[arr].append(char)
            if arr == numRows - 1:
                step = -1
            if arr == 0:
                step = 1
            arr += step
        return "".join(["".join(ar) for ar in array])


assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert Solution().convert("A", 1) == "A"
