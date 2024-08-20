# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dictionary = defaultdict(int)

        def dfs(node, level):
            if not node:
                return
            dictionary[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

            return
        dfs(root, 0)
        ind = max(dictionary)

        return dictionary[ind]
        