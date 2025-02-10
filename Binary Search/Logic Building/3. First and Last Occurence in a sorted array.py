class Solution:
    def searchRange(self, nums, target):
        def firstOccurrence(nums, target):
            n=len(nums)
            start=-1
            low=0
            high=n-1
            while (low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    start=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return start
        def lastOccurrence(nums, target):
            n=len(nums)
            end=-1
            low=0
            high=n-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    end=mid
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return end
        start= firstOccurrence(nums, target)
        end= lastOccurrence(nums, target)
        return [start, end]











