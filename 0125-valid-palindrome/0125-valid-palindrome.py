class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                result += i
        result = result.lower()
        if result == result[::-1]:
            return True
        else:
            return False