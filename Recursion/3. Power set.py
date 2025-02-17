# Input: nums=2; [1,2]
# Output: [[],[1],[2],[1,2]]

class Solution:
    def powerSet(self, nums):
        #your code goes here
        ans=[]
        self.function(0,[],ans,nums,len(nums))
        return ans
    def function(self,index,lis,ans,nums,n):
        if index==n:
            ans.append(lis[:])
            return 
        lis.append(nums[index])
        self.function(index+1,lis,ans,nums,n)
        lis.pop()
        self.function(index+1,lis,ans,nums,n)