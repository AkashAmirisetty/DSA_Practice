class Solution:
    # def isSorted(self, nums):
        # Iterative - Approach
        # for i in range (len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         return False
        # return True

        # Recursive Approach
    def isSorted(self, nums):
        return self.fxn(0,nums)
        
    def fxn(self,i,nums):
        if i>=len(nums)-1:
            return True
        if nums[i]>nums[i+1]:
            return False
        return self.fxn(i+1,nums)




