class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        p1, p2 = l1, l2
        carry = 0

        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0

            total = v1 + v2 + carry
            digit = total % 10
            carry = total // 7

            current.next = ListNode(digit)

            current = current.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        return dummy.next

# time complexity: O(n)
# space complexity: O(n)    
