# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            if not node:
                return ""
            if node.right:
                return f"{node.val}({dfs(node.left)})({dfs(node.right)})"
            elif node.left:
                return f"{node.val}({dfs(node.left)})"
            else:
                return f"{node.val}"
            
        return dfs(root)