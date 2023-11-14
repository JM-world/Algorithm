class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        val = ""
        maxx = len(strs) - 1
        for i in range(len(strs[0])):
            count = 0
            for k in range(1, len(strs)):
                if strs[0][i:i+1] != strs[k][i:i+1]:
                    return val
            val += strs[0][i]
        return val