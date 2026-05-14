"""
Doubly Linked List
Bloomberg Medium
"""

class ListNode:
    def __init__(self, val=0, next=None, prev=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class Solution:
    def flatten(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        curr = head
        stack = []

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)

                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            elif not curr.next and stack:
                node = stack.pop()
                curr.next = node
                node.prev = curr

            curr = curr.next

        return head
