from typing import Optional

from linked_list.utils import print_list

"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        set_to_delete = set()
        prev_value = None
        while curr:
            if curr.val == prev_value:
                set_to_delete.add(curr.val)
            prev_value = curr.val
            curr = curr.next

        curr = head
        new_node = ListNode(0)
        new_curr = new_node
        while curr:
            if curr.val not in set_to_delete:
                new_curr.next = ListNode(curr.val)
                new_curr = new_curr.next
            curr = curr.next

        return new_node.next


resp = Solution().deleteDuplicates(
    ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None)))))))
)
assert print_list(resp) == [1, 2, 5]

resp = Solution().deleteDuplicates(ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None))))))
assert print_list(resp) == [2, 3]
