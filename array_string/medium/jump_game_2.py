from typing import List

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], 
you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        last = 0
        maxi = 0
        count = 0
        for i in range(len(nums) - 1):
            maxi = max(maxi, i + nums[i])
            if i == last:
                last = maxi
                count += 1
        return count


assert Solution().jump([4, 1, 3, 1, 7, 1, 2, 1, 3, 1]) == 2
assert Solution().jump([2, 3, 1, 1, 4]) == 2
assert Solution().jump([2, 3, 0, 1, 4]) == 2
