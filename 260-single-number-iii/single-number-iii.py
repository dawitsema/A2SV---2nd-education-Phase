class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        one, zero = 0, 0
        ind = 0
        for i in range(31):
            if xor & 1 << i:
                ind = i
                break
        
        for num in nums:
            if num & 1 << ind:
                one ^= num
            else:
                zero ^= num
        
        return [one, zero]

        