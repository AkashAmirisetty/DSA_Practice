class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        summ=0
        if N==0:
            return 0
        if N==1:
            return 1
        summ=N+self.NnumbersSum(N-1)
        return summ
        
