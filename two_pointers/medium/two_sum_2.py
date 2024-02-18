from typing import List

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        for i in range(len(numbers) - 1, -1, -1):
            while numbers[i] + numbers[j] < target:
                j += 1
            if numbers[i] + numbers[j] == target:
                return [j + 1, i + 1]

            elif numbers[i] + numbers[j] > target:
                continue


assert Solution().twoSum(numbers=[1, 2, 7, 11, 15], target=9) == [2, 3]
assert Solution().twoSum(numbers=[2, 7, 11, 15], target=22) == [2, 4]
assert Solution().twoSum(numbers=[2, 7, 11, 15], target=26) == [3, 4]
assert Solution().twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
assert Solution().twoSum(numbers=[2, 3, 4, 5, 6, 7], target=10) == [2, 6]
assert Solution().twoSum(numbers=[2, 3, 4, 5, 6, 7, 8, 11], target=12) == [3, 7]
assert Solution().twoSum(numbers=[-1, 0], target=-1) == [1, 2]
