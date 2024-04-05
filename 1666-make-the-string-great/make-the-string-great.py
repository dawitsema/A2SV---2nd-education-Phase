class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        pt = 0
        while pt < len(s):
            if stack and stack[-1] == s[pt].swapcase():
                stack.pop()
            else:
                stack.append(s[pt])
            pt += 1
        
        return ''.join(stack)

