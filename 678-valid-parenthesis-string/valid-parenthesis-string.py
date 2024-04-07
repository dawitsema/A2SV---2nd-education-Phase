class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisks = []
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                asterisks.append(i)
            else:  
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
        
        while stack and asterisks:
            if stack[-1] < asterisks[-1]:
                stack.pop()
                asterisks.pop()
            else:
                break
        
        return not stack
