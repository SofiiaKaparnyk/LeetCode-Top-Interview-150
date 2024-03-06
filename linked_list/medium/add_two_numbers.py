from typing import Optional

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""
        while l1:
            first = str(l1.val) + first
            l1 = l1.next

        while l2:
            second = str(l2.val) + second
            l2 = l2.next

        sum = str(int(first) + int(second))
        strin = str(sum)[::-1]

        head = ListNode(0)
        curr = head
        for i in range(len(sum)):
            new_node = ListNode(int(strin[i]))
            curr.next = new_node
            curr = new_node

        return head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head = ListNode(0)
        curr = head
        while l1 or l2 or carry > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sumi = l1_val + l2_val + carry
            carry = sumi // 10
            sumi = sumi % 10
            new_node = ListNode(int(sumi))
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


Solution().addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3, None))), l2=ListNode(5, ListNode(6, ListNode(4, None))))
