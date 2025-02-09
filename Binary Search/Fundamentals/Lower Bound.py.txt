class Solution:
    def lowerBound(self, nums, x):
        n=len(nums)
        # BRUTE
        # for i in range(n):
        #     if nums[i]>=x:
        #         return i
        # OPTIMAL APPROACH
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


       


