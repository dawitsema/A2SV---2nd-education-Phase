class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        score = [0, 0]
        def dp(i, j, turn):
            if i == j:
                return nums[i]
            
            if turn == 0:
                one = nums[i] + dp(i + 1, j, 1)
                two = nums[j] + dp(i, j - 1, 1)
                
                return max(one, two)
            else:
                one = -nums[i] + dp(i + 1, j, 0)
                two = -nums[j] + dp(i, j - 1, 0)
                return min(one, two)

        
        # dp(0, len(nums) - 1, 0)
        # print(score)  
        return False if dp(0, len(nums) - 1, 0) < 0 else True

            


            