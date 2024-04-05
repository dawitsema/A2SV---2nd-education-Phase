class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2:
            return "".join(["a" for _ in range(n)])
        else:
            return "".join(["a" for _ in range(n-1)]) + "b"
        