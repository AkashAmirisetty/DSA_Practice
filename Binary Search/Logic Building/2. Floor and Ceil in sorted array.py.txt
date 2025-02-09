class Solution:
    def floor(self,nums, n, x):
        n=len(nums)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=x:
                ans=nums[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def ceil(self, nums, n, x):
        n=len(nums)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=x:
                ans=nums[mid]
                high=mid-1
            else:
                low=mid+1
        return ans
    def getFloorAndCeil(self, nums, x):
        n=len(nums)
        # low=0
        # high=n-1
        # ceil=-1
        # floor=-1
        # while low<=high:
        #     mid=(low+high)//2
        #     if nums[mid]==x:
        #         return (nums[mid], nums[mid])
        #     elif nums[mid]<x:
        #         floor=nums[mid]
        #         low=mid+1
        #     elif nums[mid]>x:
        #         ceil=nums[mid]
        #         high=mid-1
        # return (floor, ceil)
        floor=self.floor(nums,n, x)
        ceil=self.ceil(nums, n, x)
        return [floor, ceil]

        
       
