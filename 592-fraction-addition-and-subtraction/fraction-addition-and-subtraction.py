class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        numerator = 0
        denominator = 1
        

        if expression[0] != '-':
            expression = '+' + expression
        
        i = 0
        while i < len(expression):
           
            sign = 1 if expression[i] == '+' else -1
            i += 1
            
            
            num_start = i
            while expression[i] != '/':
                i += 1
            num1 = int(expression[num_start:i])
            
           
            i += 1
            denom_start = i
            while i < len(expression) and expression[i] not in ['+', '-']:
                i += 1
            num2 = int(expression[denom_start:i])
            
            
            numerator = numerator * num2 + sign * num1 * denominator
            denominator *= num2
        
        comm = gcd(abs(numerator), denominator)
        numerator //= comm
        denominator //= comm
        
      
        return f"{numerator}/{denominator}"
