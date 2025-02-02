class Solution:
    def largestElement(self, nums):
        n=len(nums)
        # for i in range(0,n):
        lar=nums[0]
        for j in range(1,n):
            if nums[j]>lar:
                lar=nums[j]
        return lar



        