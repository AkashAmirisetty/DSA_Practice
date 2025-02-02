class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        # My Approach:
        # lar= nums[0]
        # for i in range(n):
        #     if nums[i]>lar:
        #         lar=nums[i]
        # sec_lar=-1
        # for i in range(0,n):
        #     if nums[i]>sec_lar and nums[i]!=lar:
        #         sec_lar=nums[i]
        # return sec_lar

        # Most Optimized is :
        if n<2:
            return -1
        lar= nums[0]
        sec_lar=-1
        for num in nums:
            if num>lar:
                sec_lar=lar
                lar=num
            elif num>sec_lar and num!=lar:
                sec_lar=num
        return sec_lar

        