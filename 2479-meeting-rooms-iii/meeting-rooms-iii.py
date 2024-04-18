class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]
        used = []
        count = [0] * n
 
        for start, end in meetings:
            while used and used[0][0] <= start:
                end_time, room = heappop(used)
                heappush(available, room)

            if not available:
                end_time, room = heappop(used)
                end = end_time + (end - start)
                heappush(available, room)

            room = heappop(available)
            heappush(used, (end, room))
            count[room] += 1
        
        return count.index(max(count))