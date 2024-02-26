"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in map.values():
                    return False
                map[s[i]] = t[i]
            else:
                if map[s[i]] == t[i]:
                    continue
                return False
        return True


assert Solution().isIsomorphic(s="egg", t="add") is True
assert Solution().isIsomorphic(s="geg", t="add") is False
assert Solution().isIsomorphic(s="foo", t="bar") is False
assert Solution().isIsomorphic(s="paper", t="title") is True
assert Solution().isIsomorphic(s="badc", t="baba") is False
