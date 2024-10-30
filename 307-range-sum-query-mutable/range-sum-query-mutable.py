class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.lenn = 2 ** ceil(log(self.n, 2))  
        self.arr = [0] * (2 * self.lenn - 1)  
        x = self.lenn - 1
        for i in range(x, x + self.n):
            self.arr[i] = nums[i - x]

        for i in range(self.lenn - 2, -1, -1):
            self.arr[i] = self.arr[2 * i + 1] + self.arr[2 * i + 2]

    def update(self, index: int, val: int) -> None:
        indx = index + self.lenn - 1  
        diff = val - self.arr[indx]   
        self.arr[indx] = val          

        while indx > 0:
            indx = (indx - 1) // 2
            self.arr[indx] = self.arr[2 * indx + 1] + self.arr[2 * indx + 2]

    def sumRange(self, left: int, right: int) -> int:
        left += self.lenn - 1  
        right += self.lenn - 1
        ans = 0

        while left <= right:
            if left % 2 == 0:   
                ans += self.arr[left]
                left += 1
            if right % 2 == 1:  
                ans += self.arr[right]
                right -= 1
            left = (left - 1) // 2  
            right = (right - 1) // 2  

        return ans
