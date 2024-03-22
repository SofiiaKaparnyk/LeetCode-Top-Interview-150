from typing import List

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        new_interval = [intervals[0]]
        for interval in intervals:
            prev0 = new_interval[-1][0]
            prev1 = new_interval[-1][1]

            curr0 = interval[0]
            curr1 = interval[1]

            if prev1 >= curr0:
                new_interval[-1] = [min(prev0, curr0), max(prev1, curr1)]
            else:
                new_interval.append(interval)

        return new_interval


assert Solution().merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert Solution().merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
assert Solution().merge(intervals=[[1, 4], [0, 4]]) == [[0, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 1]]) == [[0, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
assert Solution().merge(intervals=[[1, 4], [0, 2], [3, 5]]) == [[0, 5]]
assert Solution().merge(intervals=[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
assert Solution().merge(intervals=[[1, 4], [5, 6]]) == [[1, 4], [5, 6]]
