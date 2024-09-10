class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        psum = 0
        count = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1


        for i in range(len(nums)):
            psum += nums[i]
            temp = psum % k
            count += hashMap[temp]
            hashMap[temp] += 1

        
        return count
            
        