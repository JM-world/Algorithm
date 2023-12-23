class Solution:
    def isPathCrossing(self, path: str) -> bool:
        num1 = 0
        num2 = 0
        list1 = [[0, 0]]
        for i in path:
            if i == 'N':
                num1 += 1
            elif i == 'S':
                num1 -= 1
            elif i == 'E':
                num2 += 1
            else:
                num2 -= 1

            
            if [num1, num2] in list1:
                return True
            
            list1.append([num1, num2])

            

        return False