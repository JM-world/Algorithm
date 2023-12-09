class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        re_score = score[:]
        re_score.sort(reverse=True)
        score[score.index(re_score[0])] = "Gold Medal"
        if len(score) >= 2:
            score[score.index(re_score[1])] = "Silver Medal"
            if len(score) >= 3:
                score[score.index(re_score[2])] = "Bronze Medal"
                
                if len(score) >= 4:
                    count = 4
                    for i in range(3, len(score)):
                        score[score.index(re_score[i])] = str(count)
                        count+=1
                    
        return score
        
        
        