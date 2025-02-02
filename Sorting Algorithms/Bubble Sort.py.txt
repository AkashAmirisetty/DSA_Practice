class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)-1,-1,-1):
            is_swapped=False
            for j in range(i):
                if nums[j+1]<nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    is_swapped=True
            if not is_swapped:
                break
        return nums
