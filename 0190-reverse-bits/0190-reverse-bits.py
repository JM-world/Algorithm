class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)
        add=32-(len(n)-2) 
        reverse_n=''
        for i in range(add):
            reverse_n+='0'
        for i in range(2,len(n)):
            reverse_n = n[i]+reverse_n
        reverse_n = '0b'+reverse_n
        ans=int(reverse_n,2)
        return ans
