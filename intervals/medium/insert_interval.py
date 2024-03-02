from typing import List

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0]:
                if i == len(intervals) - 1 or intervals[i + 1][0] > newInterval[0]:
                    intervals.insert(i + 1, newInterval)
                    break
            else:
                intervals.insert(i, newInterval)
                break

        new_int = []
        start, end = intervals[0][0], intervals[0][1]
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


assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]
assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [
    [1, 2],
    [3, 10],
    [12, 16],
]
assert Solution().insert(intervals=[[6, 9]], newInterval=[0, 0]) == [[0, 0], [6, 9]]
assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10]], newInterval=[4, 8]) == [[1, 2], [3, 10]]
assert Solution().insert(intervals=[], newInterval=[4, 8]) == [[4, 8]]
assert Solution().insert(intervals=[[1, 5]], newInterval=[2, 7]) == [[1, 7]]
assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [[1, 5], [6, 9]]
assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [
    [1, 2],
    [3, 10],
    [12, 16],
]
assert Solution().insert(intervals=[[1, 5]], newInterval=[2, 3]) == [[1, 5]]
assert Solution().insert(intervals=[[1, 5]], newInterval=[6, 8]) == [[1, 5], [6, 8]]
