class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        checker = defaultdict(int)

        for word in words2:
            temp = Counter(word)
            for ch in temp:
                checker[ch] = max(checker[ch], temp[ch])

        for word in words1:
            temp = Counter(word)
            valid = True
            for ch in checker:
                if checker[ch] > temp[ch]:
                    valid = False
                    break
            
            if valid:
                ans.append(word)
        
        
        return ans