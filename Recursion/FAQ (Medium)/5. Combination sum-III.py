# Input : k = 3 , n = 7
# Output : [ [1, 2, 4] ]
# Explanation :
# 1 + 2 + 4 = 7
# There are no other valid combinations.

class Solution:
    def combinationSum3(self, k, n):
        ans=[]
        nums=[]
        self.function(k,n,nums,ans,1)
        return ans
        #your code goes here
    def function(self, k, summ, nums, ans, last):
        if summ==0 and len(nums)==k:
            ans.append(list(nums))
            return
        if summ<0 or len(nums)>k:
            return
        for i in range(last, 10):
            if i<=summ:
                nums.append(i)
                self.function(k,summ-i,nums,ans,i+1)
                nums.pop()
            else:
                break
        