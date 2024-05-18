# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(current):
            if current == None: return 0

            left_coins = dfs(current.left)
            right_coins = dfs(current.right)

            self.moves += abs(left_coins) + abs(right_coins)

            return (current.val - 1) + left_coins + right_coins

        dfs(root)

        return self.moves