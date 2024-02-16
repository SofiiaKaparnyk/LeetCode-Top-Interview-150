"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        occ = haystack.find(needle)
        return occ


assert Solution().strStr("sadbutsad", "sad") == 0
assert Solution().strStr("leetcode", "leeto") == -1
