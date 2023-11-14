class Solution:
    def isValid(self, s: str) -> bool:
        for _ in range(len(s)):
            if s == '':
                return True
            elif '()' not in s and '{}' not in s and '[]' not in s:
                return False
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')