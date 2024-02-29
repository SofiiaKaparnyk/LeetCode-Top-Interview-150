"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for let in s:
            d_s[let] = d_s.get(let, 0) + 1
        for letter in t:
            d_t[letter] = d_t.get(letter, 0) + 1
        return d_s == d_t


assert Solution().isAnagram(s="anagram", t="nagaram") is True
assert Solution().isAnagram(s="rat", t="car") is False
assert Solution().isAnagram(s="aaca", t="ccaa") is False
