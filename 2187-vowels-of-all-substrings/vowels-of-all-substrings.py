class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cnt = 0
        n = len(word)
        for i in range(len(word)):
            if word[i] in vowels:
                cnt += (i + 1) * (n - i)
        
        return cnt 
        