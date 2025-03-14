class Solution:
    def canJump(self, nums):
        #your code goes here
        n=len(nums)
        maxind=0
        for i in range(n):
            if i>maxind:
                return False
            maxind=max(i+nums[i],maxind)
            if maxind>=n-1:
                return True


            
