# Input : nums = [1, 2, 3, 4, 5] , k = 8
# Output : Yes
# Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.
class Solution:
    def powerSet(self, nums):
        ans = []
        self.function(0, [], ans, nums,len(nums))
        return ans
    def function(self, index, lis, ans, nums, n):
        if index==n:
            ans.append(lis[:])
            return
        lis.append(nums[index])
        self.function(index+1, lis,ans,nums,n)
        lis.pop()
        self.function(index+1, lis,ans,nums,n)
    def checkSubsequenceSum(self, nums, k):
        ans=self.powerSet(nums)
        # total_sum=0
        for row in ans:
            # total_sum+=sum(row)
            if sum(row)==k:
                return True
        return False
    

