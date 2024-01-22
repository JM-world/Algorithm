class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s=s.split(" ")
        
        if len(pattern) != len(split_s) or len(set(pattern)) != len(set(split_s)):
            return False
        
        dicti = {}
        for i in range(len(pattern)):
            dicti[pattern[i]] = split_s[i]
            
        for i in range(len(pattern)):
            if dicti[pattern[i]] != split_s[i]:
                return False
        
        return True