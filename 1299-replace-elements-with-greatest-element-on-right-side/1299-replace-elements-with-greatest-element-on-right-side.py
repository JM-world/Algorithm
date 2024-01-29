class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        else:
            arr[0] = max(arr[1:])
            i = 1
            while True:
                try:
                    maxi = max(arr[i+1:])
                    maxd = i + 1 + arr[i+1:].index(maxi)
                    arr[i:maxd] = [maxi] * len(arr[i:maxd])
                    i =maxd
                except:
                    break
            arr[-1] = -1
            return arr
            
        