class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cnt = 0
        result = [[1]]
        while len(result) != numRows:
            br = []
            br.append(result[cnt][0])
            for i in range(len(result[cnt])-1):
                br.append(result[cnt][i] + result[cnt][i+1])
            br.append(result[cnt][-1])
            result.append(br)
            cnt +=1
        return result