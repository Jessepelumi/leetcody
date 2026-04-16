# Problem: #2 Add Two Numbers
# Difficulty: Medium

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0) # placeholder
        current = dummy
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2 or carry:
            # handle uneven lists
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)

            # move pointers
            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next
    
# Time complexity: O(n)
# Space complexity: O(n)
