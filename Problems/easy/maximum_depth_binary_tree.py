"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

"""
My solution:

For tree root = [3, 9, 20, null, null, 15, 7]:
root node = 3
first level's left & right = 9 & 20 respectively 
second level left's left & right = null & null
second level right's left & right = 15 & 7

To get the deepest level, do a BFS (level order traversal) and keep track of the level.
"""

# Python collections
from collections import deque

# tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maximumDepth(root: TreeNode) -> int:
        # check if the tree is empty
        if not root:
            return 0
        
        queue = deque([root])
        level = 0

        while queue:

            size = len(queue)

            for _ in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level
    
    # time & space complexity -> O(n)
