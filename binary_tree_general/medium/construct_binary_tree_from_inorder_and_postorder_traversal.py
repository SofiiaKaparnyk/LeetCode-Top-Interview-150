from binary_tree_general.utils import print_tree

from typing import List, Optional


"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is 
the postorder traversal of the same tree, construct and return the binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return

        root_val = postorder[-1]
        root = TreeNode(root_val)

        i = inorder.index(root_val)
        left_trees = inorder[:i]
        right_trees = inorder[i+1:]

        left_postorder_trees = postorder[:i]
        right_postorder_trees = postorder[i:-1]

        root.left = self.buildTree(left_trees, left_postorder_trees)
        root.right = self.buildTree(right_trees, right_postorder_trees)
        return root


sol = Solution().buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
print_tree(sol)