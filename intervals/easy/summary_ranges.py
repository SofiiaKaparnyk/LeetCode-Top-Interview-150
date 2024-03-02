from typing import List

"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x 
such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        new_ls = []
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != nums[i + 1] - 1:
                end = i
                if start == end:
                    new_ls.append(f"{nums[start]}")
                else:
                    new_ls.append(f"{nums[start]}->{nums[end]}")
                start = i + 1
        return new_ls


assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert Solution().summaryRanges([0, 1, 2, 4, 5, 7, 8]) == ["0->2", "4->5", "7->8"]
assert Solution().summaryRanges([-1]) == ["-1"]
assert Solution().summaryRanges([]) == []
