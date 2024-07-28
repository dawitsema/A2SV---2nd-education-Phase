class Solution:
    def secondMinimum(self, n, edges, time, change):
        # Create adjacency list
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # Initialize distances and frequency arrays
        dist1 = [sys.maxsize] * (n + 1)
        dist2 = [sys.maxsize] * (n + 1)
        freq = [0] * (n + 1)
        
        # Min heap to store (time_taken, node)
        min_heap = []
        heappush(min_heap, (0, 1))
        dist1[1] = 0
        
        while min_heap:
            time_taken, node = heappop(min_heap)
            freq[node] += 1
            
            # If the node is visited for the second time and is 'n', return the answer
            if freq[node] == 2 and node == n:
                return time_taken
            
            # Check if the current light is red and wait if necessary
            if (time_taken // change) % 2:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken += time
            
            for neighbor in adj[node]:
                # Ignore nodes that have already been popped out twice
                if freq[neighbor] == 2:
                    continue
                
                # Update dist1 if it's greater than the current time_taken and store its value in dist2
                if dist1[neighbor] > time_taken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = time_taken
                    heappush(min_heap, (time_taken, neighbor))
                elif dist2[neighbor] > time_taken and dist1[neighbor] != time_taken:
                    dist2[neighbor] = time_taken
                    heappush(min_heap, (time_taken, neighbor))
        
        return 0