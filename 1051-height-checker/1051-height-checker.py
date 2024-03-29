class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hei = heights[:]
        hei.sort()
        
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != hei[i]:
                cnt += 1
                
        return cnt