class Solution:
    def isHappy(self, n: int) -> bool:
        li = []
        while True:
            num = 0
            for i in str(n):
                num += int(i) * int(i)
            if num in li:
                return False
            elif num == 1:
                return True
            li.append(num)

            n = num + 1 - 1 