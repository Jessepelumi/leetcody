"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
"""

"""
My solution:

For tree p = [1, 2, 3]
root node = 1, left child = 2, and right child = 3

For two binary trees to be the same, they must have the same number of nodes and each coresponding node must hold the same value.
Traverse both trees simultaneously and compare the value of each node -> preorder traversal.
Preorder traversal: visit node -> visit left -> visit right.
"""

# define the tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSame(self, p: TreeNode, q: TreeNode) -> bool:
        # check if both trees are empty
        if not p and not q:
            return True
        
        # check if one tree is empty
        if not p or not q:
            return False
        
        # check for value mismatch
        if p.val != q.val:
            return False
        
        # traverse the tree
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
    
    # time complexity -> O(n+m) if each node is visited once. If trees are the same size, O(n)
    # space complexity -> balanced tree: O(log n). Skewed: O(n)
