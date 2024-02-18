from typing import List

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = 0
        i = len(height) - 1
        max_V = 0
        while i != j:
            min_height = min(height[i], height[j])
            V = min_height * (i - j)
            max_V = max(max_V, V)
            if height[j] < height[i]:
                j += 1
            else:
                i -= 1
        return max_V


assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert Solution().maxArea([1, 8, 6, 2, 5, 4, 5, 3, 4]) == 28
assert Solution().maxArea([1, 1]) == 1

# JS solution just for fun :)

"""
var maxArea = function(height) {
    let i = 0;
    let j = height.length - 1;
    let max_V = 0;
    while (i !== j) {
        let min_height = Math.min(height[i], height[j]);
        let V = min_height * (j - i);
        max_V = Math.max(max_V, V);
        if (height[j] < height[i]){
            j --
        }
        else {
            i ++
        }
    }
    return max_V
};
"""
