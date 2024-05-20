class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_num = 0
        last_sign = '+'
        s = s.replace(' ', '')  
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)
            
            if ch in '+-*/' or i == len(s) - 1:
                if last_sign == '+':
                    stack.append(current_num)
                elif last_sign == '-':
                    stack.append(-current_num)
                elif last_sign == '*':
                    stack.append(stack.pop() * current_num)
                elif last_sign == '/':
                    stack.append(int(stack.pop() / current_num))  
                
                last_sign = ch
                current_num = 0
        
        return sum(stack)

