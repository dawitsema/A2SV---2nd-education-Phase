class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = {}
        for word in words:
            if word not in c:
                c[word] = [-1, word]
            else:
                c[word][0] -= 1
        
        vals = [x for x in c.values()]
        heapify(vals)
        ans = []
        while k > 0:
            ans.append(heappop(vals)[1])
            k -= 1
        return ans