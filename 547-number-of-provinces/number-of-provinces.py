class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [False for _ in range(len(isConnected[0]))] 
        count = 0

        # def inbound(row, col):
        #     return (0 <= row < len(isConnected)) and (0 <= col < len(isConnected[0]))

        def dfs(node):
            visited[node] = True
            for i, ng in enumerate(isConnected[node]):
                if i != node and not visited[i] and ng == 1:
                    dfs(i)

        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                count += 1

        return count      