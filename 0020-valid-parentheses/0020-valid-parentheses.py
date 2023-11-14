class Solution:
    def isValid(self, s: str) -> bool:
        for _ in range(len(s)):
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if s == '':
                return True
        return False