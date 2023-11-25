class Solution:
    def binaryGap(self, n: int) -> int:
        num = 0
        a = bin(n)[2:]
        for _ in range(a.count('1')-1):
            if num < a[a.index('1')+1:].index('1')+1 - a.index('1'):
                num = a[a.index('1')+1:].index('1')+1 - a.index('1')
            a = a[a[a.index('1')+1:].index('1')+1 - a.index('1'):]
        return num