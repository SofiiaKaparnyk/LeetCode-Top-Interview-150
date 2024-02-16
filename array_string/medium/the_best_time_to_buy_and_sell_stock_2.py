from typing import List

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minim = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] <= minim:
                minim = prices[i]
            else:
                profit += prices[i] - minim
                minim = prices[i]
        return profit


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
assert Solution().maxProfit([1]) == 0
assert Solution().maxProfit([1, 1, 1, 1]) == 0
assert Solution().maxProfit([2, 1, 2, 0, 1]) == 2
