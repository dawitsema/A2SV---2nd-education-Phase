class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx = 0
        for group in sentences:
            maxx = max(maxx, len(group.split()))
        return maxx