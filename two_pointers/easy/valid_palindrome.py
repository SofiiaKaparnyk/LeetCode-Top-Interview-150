import re

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[,:.]", "", s)
        new_s = "".join(s.split())
        return new_s.lower() == new_s[::-1].lower()


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
        return new_s == new_s[::-1]


assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
assert Solution().isPalindrome("a.") is True
assert Solution().isPalindrome("0P") is False
assert Solution().isPalindrome("race a car") is False
assert Solution().isPalindrome(" ") is True
