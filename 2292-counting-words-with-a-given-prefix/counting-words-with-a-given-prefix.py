class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            p = True
            for j in range(len(pref)):
                if len(words[i]) < j + 1 or pref[j] != words[i][j]:
                    p = False
                    break
            
            if p:
                count += 1
        

        return count