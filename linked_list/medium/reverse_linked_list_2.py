from typing import Optional

from linked_list.utils import print_list

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the 
list from position left to position right, and return the reversed list.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        ls = []
        curr = head
        while curr:
            ls.append(curr)
            curr = curr.next

        i = 1
        curr = head
        while curr:
            if left == 1:
                new_node = self.reverse(curr, right - left)
                curr = new_node
                head = curr
                ls[left - 1].next = ls[right] if len(ls) > right else None
                break
            if i + 1 == left:
                new_node = self.reverse(curr.next, right - left)
                curr.next = new_node
                ls[left - 1].next = ls[right] if len(ls) > right else None
                break
            curr = curr.next
            i += 1

        return head

    def reverse(self, head, diff):
        curr = head
        i = 0
        prev = None
        while i <= diff:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        return prev


resp = Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 2, 5
)
assert print_list(resp) == [1, 5, 4, 3, 2, 6]

resp = Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 3, 4
)
assert print_list(resp) == [1, 2, 4, 3, 5, 6]

resp = Solution().reverseBetween(ListNode(3, ListNode(5, None)), 1, 2)
assert print_list(resp) == [5, 3]

resp = Solution().reverseBetween(ListNode(3, ListNode(5, ListNode(6, None))), 1, 2)
assert print_list(resp) == [5, 3, 6]

resp = Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, None))), 2, 3)
assert print_list(resp) == [1, 3, 2]
