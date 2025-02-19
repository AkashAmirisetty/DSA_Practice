class Solution:
    def subsetSums(self, nums):
        ans=[]
        self.function(0,[],ans,nums,len(nums))
        return ans

        
        #your code goes here
    def function(self, index, lis, ans, nums,n):
        if index==n:
            ans.append(sum(lis))
            return
        lis.append(nums[index])
        self.function(index+1, lis,ans,nums,n)
        lis.pop()
        self.function(index+1,lis,ans,nums, n)