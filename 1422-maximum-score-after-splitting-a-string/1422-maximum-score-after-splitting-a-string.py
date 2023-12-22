class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            score = 0
            score += s[:i].count('0') + s[i:].count('1')
            if result < score:
                result = score
        return result