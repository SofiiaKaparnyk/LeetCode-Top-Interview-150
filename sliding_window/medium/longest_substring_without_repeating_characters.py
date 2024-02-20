"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ""
        max_length = 0
        for i in s:
            if i not in subs:
                subs += i
                max_length = max(max_length, len(subs))
                continue
            while i in subs:
                subs = subs[1:]
            subs += i
        return max_length


assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3
assert Solution().lengthOfLongestSubstring("p") == 1
assert Solution().lengthOfLongestSubstring("") == 0
assert Solution().lengthOfLongestSubstring("au") == 2
assert Solution().lengthOfLongestSubstring("aab") == 2
assert Solution().lengthOfLongestSubstring("aabcbasd") == 5
