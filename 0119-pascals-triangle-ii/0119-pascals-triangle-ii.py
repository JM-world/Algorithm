class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        cnt = 0
        for _ in range(rowIndex):
            br = []
            br.append(result[cnt][0])
            for i in range(len(result[cnt])-1):
                br.append(result[cnt][i] + result[cnt][i+1])
            br.append(result[cnt][-1])
            result.append(br)
            cnt +=1
        return result[rowIndex]