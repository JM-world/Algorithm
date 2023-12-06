class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        money = 0
        while True:
            if n >= 7:
                for i in range(7):
                    money += i + monday
                monday += 1
                n -= 7
            else:
                for k in range(n):
                    money += k + monday
                return money