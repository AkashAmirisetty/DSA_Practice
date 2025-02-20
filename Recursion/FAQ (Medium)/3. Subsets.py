class Solution:
    def subsetSums(self, nums):
        ans=[]
        self.func(0,0,ans,nums)
        return ans

        
    def func(self,ind,sums,ans,nums):
        if ind==len(nums):
            ans.append(sums)
            return
        self.func(ind+1,sums+nums[ind],ans,nums)
        self.func(ind+1,sums,ans,nums)