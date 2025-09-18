class Solution:
    def findMin(self, nums: List[int]) -> int:
    # Brute force (using linear seacrh)
        # n=len(nums)
        # minimum=nums[0]
        # for i in range(1,n):
        #     if nums[i]<minimum:
        #         minimum=nums[i]
        # return minimum

        n=len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]



        