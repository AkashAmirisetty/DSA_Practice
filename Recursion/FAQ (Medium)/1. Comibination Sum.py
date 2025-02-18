# Input : candidates = [2, 3, 5, 4] , target = 7
# Output : [ [2, 2, 3] , [3, 4] , [5, 2] ]
# Explanation :2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 5 and 2 are candidates, and 5 + 2 = 7.
# 3 and 4 are candidates, and 3 + 4 = 7.
# There are total three combinations.
class Solution:
    def combinationSum(self, candidates, target):
        ans=[]
        self.function(0,[], target, candidates, len(candidates), ans)
        return ans
        if not ans:
            return 1
        #your code goes here
    def function(self,index, lis, target, nums, n, ans):
        if target==0:
            ans.append(lis[:])
            return 
        if target<0 or index==n:
            return 
        lis.append(nums[index])
        self.function(index, lis, target-nums[index], nums, n, ans)
        lis.pop()
        self.function(index+1, lis, target, nums, n, ans)

        