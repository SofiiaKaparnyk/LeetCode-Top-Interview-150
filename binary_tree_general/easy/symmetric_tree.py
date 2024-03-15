from typing import Optional

from binary_tree_general.utils import print_tree

"""Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.compare(root.right, root.left)

    def compare(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val != node2.val:
            return False

        resp = self.compare(node1.right, node2.left)
        resp2 = self.compare(node1.left, node2.right)
        return resp and resp2


tree = TreeNode(
    1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
)
# print_tree(tree)
assert Solution().isSymmetric(tree) is True

tree = TreeNode(1, left=TreeNode(2, right=TreeNode(3)), right=TreeNode(2, right=TreeNode(3)))
print_tree(tree)
assert Solution().isSymmetric(tree) is False
