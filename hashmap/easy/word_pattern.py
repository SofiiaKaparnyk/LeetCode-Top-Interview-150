"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        words = s.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in map:
                if words[i] in map.values():
                    return False
                map[pattern[i]] = words[i]
            else:
                if map[pattern[i]] == words[i]:
                    continue
                return False
        return True


assert Solution().wordPattern(pattern="abba", s="dog cat cat dog") is True
assert Solution().wordPattern(pattern="abba", s="dog cat cat fish") is False
assert Solution().wordPattern(pattern="aaaa", s="dog cat cat dog") is False
