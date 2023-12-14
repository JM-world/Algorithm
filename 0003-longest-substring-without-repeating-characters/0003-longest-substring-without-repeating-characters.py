class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        num = 0
        
        while True:
            
            dan = ""
            count = 0
            for i in range(len(s)):
                if s[i] not in dan:
                    dan += s[i]
                    count += 1
                else:
                    s = s[1:]
                    break
            
            if num < count:
                num = count
            
            if s == "" or len(s) < num or len(set(s)) == 1 or dan == s:
                return num