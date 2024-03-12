from typing import Optional

from linked_list.utils import print_list

"""Given the head of a linked list, rotate the list to the right by k places."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        last_node = curr

        k %= length
        if k == 0:
            return head

        curr = head
        index = length - k - 1
        for _ in range(index):
            # we iterate to the values that must be shifted
            curr = curr.next

        # assign part that should be shifted upfront to last_nodes
        last_nodes = curr.next
        # make head a next item after last_node
        last_node.next = head
        # since end was shifted, current pointer is set to None
        curr.next = None
        return last_nodes

    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if k == 0 or not head or not head.next:
    #         return head
    #
    #     for _ in range(k):
    #         head = self.rotate(head)
    #     return head
    #
    # def rotate(self, head):
    #     curr = head
    #     while curr:
    #         if curr.next.next is None:
    #             curr_head = head
    #             last_node = curr.next
    #             curr.next = None
    #             last_node.next = curr_head
    #             head = last_node
    #             return head
    #         curr = curr.next
    #     return head


resp = Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 1008)
assert print_list(resp) == [3, 4, 5, 1, 2]

resp = Solution().rotateRight([], 2)
assert print_list(resp) == []

resp = Solution().rotateRight(ListNode(1, ListNode(2, None)), 2)
assert print_list(resp) == [1, 2]
