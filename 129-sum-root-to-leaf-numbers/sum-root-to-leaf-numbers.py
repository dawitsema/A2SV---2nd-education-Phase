# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node,temp):
            nonlocal ans
            if node:
                temp = temp*10 + node.val
                if not node.left and not node.right:
                    ans += temp
                helper(node.left, temp)
                helper(node.right, temp)

        ans = 0
        helper(root,0)
        return ans
        