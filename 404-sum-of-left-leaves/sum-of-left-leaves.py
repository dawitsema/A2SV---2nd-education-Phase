# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # queue = deque([(root, False)])
        # ans = 0
        # while queue:
        #     node, isLeft = queue.popleft()
        #     if not node.left and not node.right and isLeft:
        #         ans += node.val
        #     if node.left:
        #         queue.append((node.left, True))
        #     if node.right:
        #         queue.append((node.right, False))

        # return ans 
        def dfs(node, isLeft):
            if not node: return 0
            if not node.left and not node.right and isLeft:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)

        
        