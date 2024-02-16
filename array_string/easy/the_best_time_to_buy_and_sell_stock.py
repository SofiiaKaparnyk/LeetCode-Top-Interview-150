from typing import List

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.


Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= min:
                min = prices[i]
            elif prices[i] >= max or prices[i] - min > diff:
                max = prices[i]
                diff = max - min
        if max:
            return diff
        return 0


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
