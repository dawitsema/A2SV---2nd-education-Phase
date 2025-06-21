class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        res = len(word)

        for a in count.values():
            deleted = 0
            for b in count.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            
            res = min(res, deleted)
        
        return res
