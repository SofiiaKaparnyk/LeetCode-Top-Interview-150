from binary_tree_general.utils import print_tree

from typing import List, Optional

"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
the inorder traversal of the same tree, construct and return the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root_val = preorder[0]
        root = TreeNode(root_val)

        i = inorder.index(root_val)
        left_trees = inorder[:i]
        right_trees = inorder[i + 1:]

        left_preorder_trees = preorder[1:i + 1]
        right_preorder_trees = preorder[i + 1:]

        root.left = self.buildTree(left_preorder_trees, left_trees)
        root.right = self.buildTree(right_preorder_trees, right_trees)

        return root


sol = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
print_tree(sol)

sol = Solution().buildTree(preorder=[5, 3, 2, 4, 8, 6, 7, 10, 9, 11], inorder=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print_tree(sol)
