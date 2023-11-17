class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = '0b'
        s1 = int(a, 2)
        s2 = int(b, 2)
        result = bin(s1 + s2)
        return result[2:]