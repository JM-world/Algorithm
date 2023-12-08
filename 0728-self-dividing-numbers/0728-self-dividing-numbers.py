class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lr = []
        for i in range(left, right+1):
            count = 0
            if '0' not in str(i):
                for k in range(len(str(i))):
                    if i % int(str(i)[k]) == 0:
                        count += 1
                        if count == len(str(i)):
                            lr.append(i)
        return lr