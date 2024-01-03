class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        x = 0
        y = 0
        temp = 0
        count = 0
        for i in bank:
            if i.count("1") == 0:
                continue
            elif x == 0:
                x = i.count("1")
            elif x != 0 and y == 0:
                y = i.count("1")
            if x != 0 and y != 0:
                temp += x * y
                if count % 2 == 0:
                    x = 0
                    count += 1
                else:
                    y = 0
                    count += 1
        return temp
        