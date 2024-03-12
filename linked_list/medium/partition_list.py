from typing import Optional

from linked_list.utils import print_list

"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        more = ListNode(0)
        curr_less = less
        curr_more = more
        curr = head
        while curr:
            if curr.val < x:
                curr_less.next = curr
                curr_less = curr_less.next
            else:
                curr_more.next = curr
                curr_more = curr_more.next
            curr = curr.next

        curr_more.next = None
        curr_less.next = more.next
        return less.next


resp = Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2, None)))))), 3)
assert print_list(resp) == [1, 2, 2, 4, 3, 5]
resp = Solution().partition(ListNode(1, None), 0)
assert print_list(resp) == [1]
