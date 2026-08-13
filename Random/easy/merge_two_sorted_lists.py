"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

"""
My solution:

- Handle empty list -> if one list is empty, return the non-empty list as the merged list, and if both are empty, return empty list.
- Traverse the lists using pointers -> p1 for list1 and p2 for list2
- Create a dummy node to keep track of the merged list -> current
- Compare the value of p1 with that of p2 and attach the smaller one to current
- After attaching, move p1 or p2, and current
"""

# define the node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Merge:
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
        dummy = Node(0)
        current = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1 # attach p1 to current
                p1 = p1.next # move p1 foward
            else:
                current.next = p2 # attach p2 to current
                p2 = p2.next # move p2 foward

            # move the current pointer
            current = current.next

        # take care of remaining nodes if either list isn't empty
        if p1:
            current.next = p1
        else:
            current.next = p2

        return dummy.next
    
    # time complexity -> O(n+m)
    # space complexity -> O(1)
