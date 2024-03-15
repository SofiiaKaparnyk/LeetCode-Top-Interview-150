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
        if not head.next or not left or not right:
            return head

        curr = head
        d = {}
        i = 1
        while curr:
            d[i] = curr
            i += 1
            curr = curr.next

        curr = head
        i = 1
        while curr:
            if i == left:
                reversed_list = self.reverse(curr, right - left) # 5,4,3,2
                if left == 1:
                    head = reversed_list
                else:
                    d[i-1].next = reversed_list
                curr.next = d.get(right+1)
                break
            curr = curr.next
            i += 1

        return head

    def reverse(self, root, i):
        prev = None
        curr = root
        while i >= 0:
            following = curr.next
            curr.next = prev
            prev = curr
            curr = following
            i -= 1
        return prev


resp = Solution().reverseBetween(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 2, 5
)
print(print_list(resp))

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
