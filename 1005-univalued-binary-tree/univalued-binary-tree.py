# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            nonlocal st
            if not node:
                return True
            
            if node.val != st:
                return False
            temp = True
            temp = temp and traverse(node.left)
            temp = temp and traverse(node.right)

            return temp
        
        st = root.val
        return traverse(root)

            
        