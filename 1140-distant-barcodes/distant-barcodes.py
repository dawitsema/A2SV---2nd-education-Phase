class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqMap = Counter(barcodes)
        heap = []
        for key, val in freqMap.items():
            heapq.heappush(heap, [-val, key])

        ans = []
        while heap:
            val1, key1 = heapq.heappop(heap)
            if not ans or ans[-1] != key1:
                ans.append(key1)
                if val1 + 1 != 0:
                    heapq.heappush(heap, [val1 + 1, key1])
            elif ans and heap and ans[-1] == key1:
                val2, key2 = heapq.heappop(heap)
                ans.append(key2)
                if val2 + 1 != 0:
                    heapq.heappush(heap, [val2 + 1, key2])
                ans.append(key1)
                if val1 + 1 != 0:
                    heapq.heappush(heap, [val1 + 1, key1])

        return ans


        
        