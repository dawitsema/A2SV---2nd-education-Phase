class Solution:
    def maxFreqSum(self, s: str) -> int:
        def is_vowel(char):
            return char.lower() in 'aeiou'

        lettersFreq = Counter(s)

        vowelFreq, consoFreq = 0, 0
        for letter, freq in lettersFreq.items():
            if is_vowel(letter):
                vowelFreq = max(vowelFreq, freq)
            else:
                consoFreq = max(consoFreq, freq)


        return vowelFreq + consoFreq