class Solution:
    def upperBound(self, nums, x):
        n= len(nums)
        # BRUTE FORCE
        # for i in range(n):
        #     if nums[i]>x:
        #         return i
        # OPTIMAL SOLUTION
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid= (low+high)//2
            if nums[mid]>x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        