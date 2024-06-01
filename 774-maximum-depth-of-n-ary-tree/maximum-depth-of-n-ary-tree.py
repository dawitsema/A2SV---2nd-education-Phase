"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            val = 0
            for child in node.children:
                val = max(val, dfs(child)) 
            
            return 1 + val

        return dfs(root)
