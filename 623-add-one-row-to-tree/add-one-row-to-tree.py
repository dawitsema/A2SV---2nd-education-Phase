# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node: return
            if d == depth - 1:
                temp1 = node.left
                temp2 = node.right
                newNode1 = TreeNode(val)
                newNode2 = TreeNode(val)
                newNode1.left = temp1
                newNode2.right = temp2
                node.left = newNode1
                node.right = newNode2
                return
            dfs(node.left, d+1)
            dfs(node.right, d+1)
            
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            root = newNode
        else:
            dfs(root, 1)
        return root