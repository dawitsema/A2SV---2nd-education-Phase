class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append((ch, i))
            elif ch == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((ch, i))
                    
        ans = []
        stack = set(stack)
        for i, ch in enumerate(s):
            if (ch, i) not in stack:
                ans.append(ch)


        return "".join(ans)

        