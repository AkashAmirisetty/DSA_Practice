class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.first(nums,target)
        last=self.last(nums,target)
        return [first, last]
    
    def first(self, nums, target):
        ans=-1
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans
    def last(self,nums,target):
        ans=-1
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans
    
        