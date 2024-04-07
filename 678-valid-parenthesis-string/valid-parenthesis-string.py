class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        asterisks = []
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == '*':
                asterisks.append(i)
            else:  # ch is ')'
                if stack:
                    stack.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
        
        # Match remaining '(' and '*' with ')'
        while stack and asterisks:
            if stack[-1] < asterisks[-1]:
                stack.pop()
                asterisks.pop()
            else:
                break
        
        return not stack
