from typing import List

"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith
paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the
given researcher has published at least h papers that have each been cited at least h times.
"""


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxi = len(citations)
        citations.sort()
        while maxi > 0:
            for i in citations:
                if i >= maxi:
                    return maxi
                else:
                    maxi -= 1
        return maxi


assert Solution().hIndex([3, 0, 6, 1, 5]) == 3
assert Solution().hIndex([1, 3, 1]) == 1
assert Solution().hIndex([100]) == 1
assert Solution().hIndex([0, 0]) == 0
