class Solution:
    def findMin(self, arr):
        # Linear search
        # n=len(nums)
        # mini=nums[0]
        # for i in range(n):
        #     if nums[i]<mini:
        #         mini=nums[i]
        # return mini
        # Binary Search
        n=len(arr)
        low=0
        high=n-1
        ans=arr[0]
        while low<=high:
            mid=(low+high)//2
            if arr[low]<=arr[mid]:
                ans=min(ans, arr[low])
                low=mid+1
            # Right side element bigger
            elif arr[low]>arr[mid]:
                ans=min(ans, arr[mid])
                high=mid-1
        return ans


           
