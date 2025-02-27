class Solution:
    def arraySum(self, nums):
        #MY Approach
        # n=len(nums)
        # if n==0:
        #     return 0
        # if n==1:
        #     return nums[0]
        # summ=nums[0]+self.arraySum(nums[1:])
        # return summ

        # Tree Approach(Striver's)
        return self.fxn(0,nums,len(nums))
    def fxn(self,i,nums,n):
        if i>=n:
            return 0
        return nums[i]+self.fxn(i+1,nums,n)