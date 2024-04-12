class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [height[0]]
        for i in range(1, len(height)):
            maxleft.append(max(maxleft[-1], height[i]))
        
        maxright = [height[-1]]
        for i in range(len(height) - 2, -1, -1):
            maxright.append(max(maxright[-1], height[i]))
        
        maxright = maxright[::-1]

        ans = 0
        for i in range(len(height)):
            ans += max(0, min(maxright[i], maxleft[i])-height[i])

        return ans
            
            