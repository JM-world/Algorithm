class Solution:
    def romanToInt(self, s: str) -> int:
        s=s.replace("IV","IIII")
        s=s.replace("IX","VIIII")
        s=s.replace("XL","XXXX")
        s=s.replace("XC","LXXXX")
        s=s.replace("CD","CCCC")
        s=s.replace("CM","DCCCC")
        sum = 0
        for i in s:
            if i == 'I':
                sum += 1
            elif i == 'V':
                sum += 5
            elif i == 'X':
                sum += 10
            elif i == 'L':
                sum += 50
            elif i == 'C':
                sum += 100
            elif i == 'D':
                sum += 500
            else:
                sum += 1000
        return sum