class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1

        for i in range(len(nums)):
            psum += nums[i]
            x = psum - k
            count += hashmap[x]
            hashmap[psum] += 1

        return count

