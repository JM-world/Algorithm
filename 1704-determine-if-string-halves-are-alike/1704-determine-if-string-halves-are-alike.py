class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        alike = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        half = int(len(s)/2)
        
        a = s[:half]
        b = s[half:]
        a_cnt = 0
        b_cnt = 0
        
        for i in range(half):
            if a[i] in alike:
                a_cnt += 1
            if b[i] in alike:
                b_cnt += 1
        
        if a_cnt == b_cnt:
            return True
        else:
            return False