from typing import List

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            if n >= gas:
                gas = n
            gas -= 1
        return True


assert Solution().canJump([2, 3, 1, 1, 4]) is True
assert Solution().canJump([3, 2, 1, 0, 4]) is False
