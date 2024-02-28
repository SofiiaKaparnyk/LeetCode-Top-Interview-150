from typing import List

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such 
that nums[i] == nums[j] and abs(i - j) <= k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False

        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map and abs(i - hash_map[nums[i]]) <= k:
                return True
            hash_map[nums[i]] = i
        return False


assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3) is True
assert Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) is True
assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2) is False
assert Solution().containsNearbyDuplicate(nums=[99, 99], k=2) is True
assert Solution().containsNearbyDuplicate(nums=[2, 2], k=3) is True
