"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


class Solution:
    def calculate(self, s: str) -> int:
        operations = ["+", "-", "*", "/"]
        stack = list()
        s = s.replace(" ", "")
        for i, char in enumerate(s):
            ...


print(Solution().calculate(s="1 + 1"))
print(Solution().calculate(s=" 2-1 + 2 "))
# print(Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)"))
