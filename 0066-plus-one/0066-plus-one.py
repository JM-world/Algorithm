class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            temp = ''
            result = []
            for i in digits:
                temp += str(i)
            for k in str(int(temp) + 1):
                result.append(int(k))
            return result
        else:
            digits[-1] = digits[-1] + 1
            return digits