from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxi = 1
        counter = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                counter = 1
            maxi = max(maxi, counter)
        return maxi


assert Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
assert Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert Solution().longestConsecutive(nums=[0]) == 1
assert Solution().longestConsecutive(nums=[]) == 0
assert Solution().longestConsecutive(nums=[1, 2, 0, 1]) == 3
assert Solution().longestConsecutive(nums=[0, 0]) == 1
assert Solution().longestConsecutive(nums=[1, 0, -1]) == 3
assert Solution().longestConsecutive(nums=[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7
