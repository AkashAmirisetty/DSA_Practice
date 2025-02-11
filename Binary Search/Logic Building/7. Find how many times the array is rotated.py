class Solution:
    def findKRotation(self, nums):
        # Linear search
        # n=len(nums)
        # ans=nums[0]
        # for i in range(n):
        #     if nums[i]<ans:
        #        return i
        # Using Binary Search
        n=len(nums)
        low=0
        high=n-1
        ans=float('inf')
        index=-1
        while (low<=high):
            mid=(low+high)//2
            if nums[low]<=nums[high]:
                if nums[low]<ans:
                    index=low
                    ans=nums[low]
                break
            if nums[low]<=nums[mid]:
                index=low
                ans=nums[low]
                low=mid+1
            elif nums[low]>nums[mid]:
                index=mid
                ans=nums[mid]
                high=mid-1
        return index
                
    
        
            