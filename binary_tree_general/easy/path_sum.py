from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        targetSum = targetSum - root.val

        resp1 = self.hasPathSum(root.left, targetSum)
        resp2 = self.hasPathSum(root.right, targetSum)
        return resp1 or resp2

tree = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1))))
assert Solution().hasPathSum(tree, 22) is True

tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
assert Solution().hasPathSum(tree, 7) is False

