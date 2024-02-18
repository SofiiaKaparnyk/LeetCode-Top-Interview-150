"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        start = 0

        for i in range(len(s)):
            for j in range(start, len(t)):
                if t[j] == s[i]:
                    start = j + 1
                    if i != len(s) - 1 and start >= len(t):
                        return False
                    break
                if j == len(t) - 1:
                    return False
        return True


assert Solution().isSubsequence(s="abc", t="ahbgdc") is True
assert Solution().isSubsequence(s="abc", t="") is False
assert Solution().isSubsequence(s="aabc", t="ahbgdc") is False
assert Solution().isSubsequence(s="axc", t="ahbgdc") is False
assert Solution().isSubsequence(s="acb", t="ahbgdc") is False
