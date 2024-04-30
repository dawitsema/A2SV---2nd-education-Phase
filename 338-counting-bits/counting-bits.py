class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]* (num + 1)
        for i in range(1, num + 1):
            if i % 2:
                ans[i] = (ans[i - 1] + 1)
            else:
                ans[i] = (ans[i // 2])
        return ans

        ans = [0]*(num+1)
        for i in range(num+1):
            count = 0
            j = i
            while i > 0:
                if i & 1:
                    count += 1
                i >>= 1
            
            ans[j] = count
        
        return ans