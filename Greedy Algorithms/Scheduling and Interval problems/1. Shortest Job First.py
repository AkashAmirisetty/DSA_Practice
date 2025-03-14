class Solution:
    def solve(self, bt):
        #your code goes here
        n=len(bt)
        bt.sort()
        waiting=0
        time=0
        for i in range(n):
            waiting+=time
            time+=bt[i]
        return waiting//n
        