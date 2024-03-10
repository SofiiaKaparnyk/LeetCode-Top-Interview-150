"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any
node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers in the original list and copied list represent the same
list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two
nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented
as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        map = {}
        curr_head = head
        while curr_head:
            # add old Node as a key to the map, it has val, next and random; and add new Node as a value
            map[curr_head] = Node(curr_head.val)
            curr_head = curr_head.next

        curr_head = head
        while curr_head:
            copied_node = map[curr_head]
            # curr_head.next and random are Nodes that are stored in the map, because we iterated through all of them
            copied_node.next = map.get(curr_head.next)
            copied_node.random = map.get(curr_head.random)
            curr_head = curr_head.next

        return map[head]


def print_linked_list_with_random(head):
    while head:
        random_val = head.random.val if head.random else None
        next_val = head.next.val if head.next else None
        print(f"[{head.val}, next:{next_val}, random:{random_val}] -> ", end="")
        head = head.next
    print("None")


# Create original linked list
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

node1.random = node3
node2.random = node1
node3.random = node4
node4.random = node2

# Print original linked list
print("Original linked list:")
print_linked_list_with_random(node1)

# Deep copy the linked list
copied_head = Solution().copyRandomList(node1)

# Print copied linked list
print("\nCopied linked list:")
print_linked_list_with_random(copied_head)
