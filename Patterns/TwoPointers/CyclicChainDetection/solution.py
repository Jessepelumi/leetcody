"""
Brute-force approach:
1. Iterate through the list and store seen nodes in a set
2. Check the set on every iteration for already seen nodes
3. If we come accross an already seen node, it is cyclic

This leads to time and space complexities of O(n)

Optimal approach - optimize for space:
1. Iterate through the list with two pointers -> slow & fast
2. Fast pointer goes one step faster than the slow pointer
3. A cycle exists when the fast and slow pointer meet at some point in the cycle
4. If the fast pointer reaches null or exists the loop, there is no cycle
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def is_cyclic(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
