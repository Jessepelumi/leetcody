# Problem: 1448. Count Good Nodes in Binary Tree
# Difficulty: Medium

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def good_node(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val):
            if not node:
                return 0
            
            is_good = 1 if node.val >= max_val else 0
            new_max = max(node.val, max_val)

            # Add all the good nodes
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)
            
        return dfs(root, float('-inf')) # '-inf' is negative infinity
    
# Time complexity: O(n)
# Space complexity O(n)

