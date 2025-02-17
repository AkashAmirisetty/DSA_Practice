class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        return self.function(0,nums,k)
        #your code goes here
    def function(self, index,nums,k):
        n=len(nums)
        if k==0:
            return 1
        if k<0 or index==n:
            return 0
        path1=self.function(index+1, nums, k-nums[index])
        path2=self.function(index+1, nums, k)
        return path1+path2