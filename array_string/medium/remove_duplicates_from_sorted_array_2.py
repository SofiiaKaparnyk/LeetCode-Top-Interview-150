from typing import List, Tuple

"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique 
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the 
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""



class Solution:
    def removeDuplicates(self, nums: List[int]) -> Tuple[int, List[int]]:
        i = 0
        d = {}
        while i != len(nums):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] <= 2:
                i += 1
            else:
                nums.remove(nums[i])
        return len(nums), nums

assert Solution().removeDuplicates([1,1,1,2,2,3]) == (5, [1,1,2,2,3])
assert Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]) == (7, [0,0,1,1,2,3,3])
assert Solution().removeDuplicates([1,1,1]) == (2, [1,1])
