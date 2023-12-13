class Solution:
    def judgeCircle(self, moves: str) -> bool:
        num1 = 0
        num2 = 0
        for i in moves:
            if i == "U":
                num1 += 1
            elif i == "D":
                num1 -= 1
            elif i == "R":
                num2 += 1
            else:
                num2 -= 1
        
        if num1 == 0 and num2 == 0:
            return True
        else:
            return False