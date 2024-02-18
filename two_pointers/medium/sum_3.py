from typing import List, Tuple

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[Tuple[int]]:
        j = 0
        i = len(numbers) - 1
        target_set = set()
        while j < i:
            if numbers[i] + numbers[j] == target:
                target_set.add((numbers[j], numbers[i]))
                j += 1
                i -= 1

            elif numbers[i] + numbers[j] < target:
                j += 1

            elif numbers[i] + numbers[j] > target:
                i -= 1

        return list(target_set)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_3 = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                return sum_3

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target_arr = self.twoSum(nums[i + 1 :], -nums[i])
            if target_arr:
                for arr in target_arr:
                    sum_3.append([arr[0], arr[1], nums[i]])
        return sum_3


assert Solution().threeSum(nums=[1, 2, -2, -1]) == []
assert Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]) == [[0, 1, -1], [-1, 2, -1]]
assert Solution().threeSum(nums=[-1, 0, 1, 2, -2, 2, -1, -4]) == [
    [2, 2, -4],
    [0, 2, -2],
    [0, 1, -1],
    [-1, 2, -1],
]
assert Solution().threeSum(nums=[0, 1, 1]) == []
assert Solution().threeSum(nums=[0, 0, 0]) == [[0, 0, 0]]
assert Solution().threeSum(nums=[0, 0, 0, 0]) == [[0, 0, 0]]
assert Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [
    [1, 3, -4],
    [0, 4, -4],
    [1, 2, -3],
    [0, 3, -3],
    [-1, 4, -3],
    [0, 2, -2],
    [-1, 3, -2],
    [0, 1, -1],
    [-1, 2, -1],
]
