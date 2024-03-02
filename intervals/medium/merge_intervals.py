from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_int = []
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if i == len(intervals) - 1 or end < intervals[i + 1][0]:
                new_int.append([start, end])
                if i != len(intervals) - 1:
                    start = intervals[i + 1][0]
                    end = intervals[i + 1][1]
            else:
                end = max(end, intervals[i + 1][1])
                start = min(start, intervals[i + 1][0])
        return new_int


assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert Solution().merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
assert Solution().merge(intervals=[[1, 4], [0, 4]]) == [[0, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 1]]) == [[0, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
assert Solution().merge(intervals=[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
assert Solution().merge(intervals=[[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
