# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        def dfs(node, is_root):
            if not node:
                return None
            
            if node.val in to_delete:
                dfs(node.left, is_root=True)
                dfs(node.right, is_root=True)
                
                return None
            else:
                if is_root:
                    ans.append(node)
                
                node.left = dfs(node.left, is_root=False)
                node.right = dfs(node.right, is_root=False)
                
                return node

        dfs(root, is_root=True)

        return ans