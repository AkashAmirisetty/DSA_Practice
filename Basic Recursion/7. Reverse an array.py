class Solution:
    def reverseArray(self, nums):
        self.fxn(0,len(nums)-1,nums)
        return nums
    def fxn(self,l,r,nums):
        if l>=r:
            return
        nums[l],nums[r]=nums[r],nums[l]
        return self.fxn(l+1,r-1,nums)
