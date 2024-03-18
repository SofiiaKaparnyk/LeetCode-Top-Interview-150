from typing import Optional

from binary_tree_general.utils import print_tree

"""Given the root of a binary tree, invert the tree, and return its root."""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        next_right = root.right
        next_left = root.left
        root.left = next_right
        root.right = next_left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


tree = TreeNode(
    4, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9))
)
sol = Solution().invertTree(tree)

print_tree(sol)
