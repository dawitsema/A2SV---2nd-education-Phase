class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        

        ans = []
        carry = 1
        for i in range(len(digits) -1, -1, -1):
            if digits[i] + carry == 10:
                ans.append(0)
                carry = 1
            else:
                ans.append(digits[i] + carry)
                carry = 0
        
        if carry == 1:
            ans.append(1)

        return ans[::-1]
                