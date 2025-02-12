import math
class Solution:
    def sum_val(self, nums, j):
        summ=0
        for num in nums:
            summ+=math.ceil(num/j)
        return summ
    def minimumRateToEatBananas(self, nums, h):
        # Brute Force Solution
        n=len(nums)
        # maxi=max(nums)
        # for divisor in range(1,maxi+1):
        #     sum_val=0
        #     for i in range(n):
        #         sum_val+= math.ceil(nums[i]/divisor)
        #     if sum_val<=h:
        #         return divisor

        # Optimal-Solution
        low=1
        high=max(nums)
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if self.sum_val(nums,mid)<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans






       