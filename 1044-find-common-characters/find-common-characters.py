class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ref = Counter(words[0])
        for word in words[1:]:
            temp = Counter(word)
            for ch in ref:
                ref[ch] = min(temp[ch], ref[ch])
                
        ans = ""
        for ch, k in ref.items():
            ans += ch * k
      
        return list(ans)