"""
Linked List, Recursion
LeetCode Easy
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next

            current = current.next

        if p1:
            current.next = p1
        else:
            current.next = p2

        return dummy.next
