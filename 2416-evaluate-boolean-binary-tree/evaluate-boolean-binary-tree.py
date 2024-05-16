# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            if node.val == 2:
                return dfs(node.left) or dfs(node.right)
            if node.val == 3:
                return dfs(node.left) and dfs(node.right)

        return dfs(root)
            
        