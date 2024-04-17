# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        word = []
        def dfs(node, s):
            if not node: return
            if not node.right and not node.left:
                s = chr(97 + node.val) + s
                word.append(s)
                return
            else:
                s = chr(97 + node.val) + s
            dfs(node.left, s)
            dfs(node.right, s)
        
        dfs(root, "")
        
        return min(word)