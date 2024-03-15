from typing import Optional

"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not q or not p:
            return False

        if p.val != q.val:
            return False

        resp1 = self.isSameTree(p.left, q.left)
        resp2 = self.isSameTree(p.right, q.right)

        return resp1 and resp2


tree = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
print(Solution().isSameTree(tree, tree))  # true
print(Solution().isSameTree(TreeNode(1, left=TreeNode(2)), TreeNode(1, right=TreeNode(2))))  # false
