class Solution:
    def linearSearch(self, nums, target):
        n=len(nums)
        for i in range(0,n):
            if target==nums[i]:
                return i
        return -1