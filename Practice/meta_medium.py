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

"""3. Longest Substring Without Repeating Characters"""
"""
s = "abcabcbb"
op = 3

bcaabcbb; seen = (bca)
 ^
   ^

- sliding window
- left pointer: shrink the window when there's a duplicate char
- right pointer: expand the window
- store seen characters
- keep count of the window size
"""
def longest_substring(s: str) -> int:
    left = 0
    max_window = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        window = right - left + 1
        max_window = max(max_window, window)

    return max_window
