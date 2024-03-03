"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "{": "}",
            "(": ")",
            "[": "]",
        }
        ls = []
        for char in s:
            if d.get(char):
                ls.append(d[char])
            else:
                if not ls or ls.pop() != char:
                    return False

        return len(ls) == 0


assert Solution().isValid("()") is True
assert Solution().isValid("()[]{}") is True
assert Solution().isValid("(]") is False
assert Solution().isValid("([)]") is False
