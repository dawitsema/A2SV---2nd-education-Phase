class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]

        for i in range(2, numRows + 1):
            temp = [1]
            for j in range(1, i):
                if len(ans[-1]) == j:
                    temp.append(1)
                else:
                    temp.append(ans[-1][j - 1] + ans[-1][j])
            
            ans.append(temp)

        
        return ans



        return ans
        
