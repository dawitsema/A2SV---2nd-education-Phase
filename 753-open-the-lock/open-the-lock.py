class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        def children(n):
            r = []
            for i in range(4):
                digit = str((int(n[i]) + 1) % 10)
                r.append(n[:i] + digit + n[i+1:])
                digit = str((int(n[i]) + 9) % 10)
                r.append(n[:i] + digit + n[i+1:])
            return r

        queue = deque([("0000", 0)])
        visited = set(deadends)
        while queue:
            node, turn = queue.popleft()
            if target == node:
                return turn
            for child in children(node):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turn + 1))


        return -1
