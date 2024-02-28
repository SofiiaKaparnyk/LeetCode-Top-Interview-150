"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    """Solution with hashmap"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}

        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1

        for let in ransomNote:
            if let in letters and letters[let] > 0:
                letters[let] -= 1
            else:
                return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        if len(magazine) == 0:
            return False

        for letter in ransomNote:
            if letter not in magazine:
                return False
            for i in range(len(magazine)):
                if letter == magazine[i]:
                    count += 1
                    if i != len(magazine) - 1:
                        magazine = magazine[:i] + magazine[i + 1 :]
                    break
        return count == len(ransomNote)


assert Solution().canConstruct(ransomNote="aa", magazine="ab") is False
assert Solution().canConstruct(ransomNote="aa", magazine="aab") is True
assert Solution().canConstruct(ransomNote="baa", magazine="aab") is True
