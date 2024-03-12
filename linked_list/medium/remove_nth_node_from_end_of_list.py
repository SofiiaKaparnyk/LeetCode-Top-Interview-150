from typing import Optional

from linked_list.utils import print_list

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        index = length - n
        i = 0
        curr = head
        while curr:
            if index == 0:
                return curr.next

            if i + 1 == index:
                curr.next = curr.next.next
            curr = curr.next
            i += 1

        return head


resp = Solution().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 6
)
assert print_list(resp) == [2, 3, 4, 5, 6]

resp = Solution().removeNthFromEnd(ListNode(1, None), 1)
assert print_list(resp) == []
