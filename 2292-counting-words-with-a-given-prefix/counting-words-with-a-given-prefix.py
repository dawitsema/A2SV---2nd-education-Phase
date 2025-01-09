class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefLen = len(pref)
        count = 0

        for i in range(len(words)):
            if len(words[i]) >= prefLen and words[i][:prefLen] == pref:
                count += 1
        

        return count