class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def bfs(node):
            queue = deque([node])
            while queue:
                v = queue.popleft()
                visited.add(v)
                for ng in rooms[v]:
                    if ng not in visited:
                        queue.append(ng)
                
        visited = set()
        count = 0     
        for i in range(len(rooms)):
            if i not in visited:
                bfs(i)
                count += 1
        

        return False if count > 1 else True
