class Solution:
    def search(self, nums, target):
        # Linear search approach
        # index=-1
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==target:
        #         index=i 
        # return index
        # BINARY SEARCH APPROACH
        n= len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                high=mid-1
            elif target>nums[mid]:
                low=mid+1
        return (-1)

        

