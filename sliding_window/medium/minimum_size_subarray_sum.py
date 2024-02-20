from typing import List

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        total = 0
        start_index = 0
        min_steps = len(nums)

        for index, num in enumerate(nums):
            total += num

            while total >= target:
                min_steps = min(index - start_index + 1, min_steps)
                total -= nums[start_index]
                start_index += 1

        return min_steps


assert Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(target=4, nums=[1, 4, 4]) == 1
assert Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]) == 3
