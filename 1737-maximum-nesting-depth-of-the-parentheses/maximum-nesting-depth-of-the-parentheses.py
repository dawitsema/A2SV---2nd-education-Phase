class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxx = temp = 0

        for st in s:
            if st == "(":
                stack.append(st)
                temp += 1
            elif st == ")":
                stack.pop()
                temp -= 1
            maxx = max(maxx, temp)
        
        return maxx

        