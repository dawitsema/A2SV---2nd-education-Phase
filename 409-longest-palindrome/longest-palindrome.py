class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary = Counter(s)
        count, flag = 0, 0
        for key in dictionary:
            if dictionary[key] % 2 == 0:
                count += dictionary[key]
            else:
                if flag == 0:
                    count += dictionary[key]
                    flag = 1
                else:
                    count += dictionary[key] - 1
        
        return count
