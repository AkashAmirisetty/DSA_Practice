class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        # Linear search
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==k:
        #         return True
        # return False
        # Using binary Search
        n= len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==k:
                return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            # Left sorted
            if nums[low]<=nums[mid]:
                if nums[low]<=k<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            # Right sorted
            else:
                if nums[mid]<=k<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False

                    
            

            