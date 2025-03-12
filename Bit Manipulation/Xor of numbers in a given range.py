class Solution:      
    def findRangeXOR(self, l, r):
        return self.xor(l-1)^self.xor(r)

        
# -----------Brute force -------------------
        # ans=0
        # for i in range(l,r+1):
        #     ans=ans^i 
        # return ans
    def xor(self,N):
        if N%4==1:
            return 1
        elif N%4==2:
            return N+1
        elif N%4==3:
            return 0
        else:
            return N 


