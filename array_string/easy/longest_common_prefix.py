from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for string in strs:
            if string.startswith(common):
                continue
            while not string.startswith(common):
                common = common[:-1]
                if len(common) == 0:
                    return ""
        return common


assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonPrefix(["flower", "flower", "flower"]) == "flower"
assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
