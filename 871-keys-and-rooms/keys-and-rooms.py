class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()

        while stack:
            node = stack.pop()
            visited.add(node)
            for ng in rooms[node]:
                if ng not in visited:
                    stack.append(ng)

        return len(visited) == len(rooms)
        