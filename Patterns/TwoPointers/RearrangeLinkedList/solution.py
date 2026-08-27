"""
1 -> 2 -> 3 -> 4 -> 5
1. Split the list into two lists at the center
2. Reverse the second list
3. Weave the two lists together by inserting consecutive values of the second list 
    after consecutive values of the first list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rearrange_list(self, head: ListNode) -> ListNode:

        # helper function to find mid-point
        def _split_list(node: ListNode) -> ListNode:
            slow = node
            fast = node

            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            second = slow.next
            slow.next = None
            return second

        # helper function to reverse second
        def _reverse_list(node: ListNode) -> ListNode:
            curr = node
            prev = None

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        def _weave_lists(first: ListNode, second: ListNode) -> ListNode:
            f = first
            s = second

            while s:
                f_temp = f.next
                s_temp = s.next

                f.next = s
                s.next = f_temp

                f = f_temp
                s = s_temp

            return first

        first = head
        second = _split_list(head)
        reversed_second = _reverse_list(second)

        return _weave_lists(first, reversed_second)
