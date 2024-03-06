from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head

        while list1 or list2:
            if list1 and (not list2 or list1.val < list2.val):
                new_node = ListNode(list1.val)
                curr.next = new_node
                curr = new_node
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                curr.next = new_node
                curr = new_node
                list2 = list2.next
        return head.next


Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(1, ListNode(3, ListNode(4, None))))
