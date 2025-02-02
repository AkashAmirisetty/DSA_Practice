class Solution:
    def selectionSort(self, nums):
        for i in range(0,len(nums)-1):
            min_index=i 
            for j in range(i, len(nums)):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]
        return nums
