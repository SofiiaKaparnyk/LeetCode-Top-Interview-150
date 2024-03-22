from binary_tree_general.utils import print_tree

"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return

        current = root
        queue = [current]
        ls = []
        i = 0
        while len(queue) > 0:
            length = len(queue)
            prev = Node()
            for _ in range(length):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                    prev.next = current.left
                    prev = current.left
                if current.right:
                    queue.append(current.right)
                    prev.next = current.right
                    prev = current.right

        return root


tree = Node(1, left=Node(2, left=Node(4, right=Node(21))), right=Node(3, left=Node(6), right=Node(7, right=Node(9))))
sol = Solution().connect(tree)
print_tree(sol)


def print_tree_with_next(root):
    if not root:
        return

    print(f"Node value: {root.val}, Next pointer: {root.next.val if root.next else None}")
    print_tree_with_next(root.left)
    print_tree_with_next(root.right)


print_tree_with_next(sol)
