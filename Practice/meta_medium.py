"""2. Add Two Numbers"""
"""
l1 = 2, 4, 3
l2 = 5, 6, 4
op = 7, 0, 8

- dummy
- current
- carry
"""
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def add_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


