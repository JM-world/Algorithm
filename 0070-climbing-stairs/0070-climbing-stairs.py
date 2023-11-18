class Solution:
    def climbStairs(self, n:int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n+1):
            tmp = a + b
            a = b
            b = tmp
        return b