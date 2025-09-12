class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# Approach 1
        temp1=[]
        temp2=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                temp1.append(nums[i])
            else:
                temp2.append(nums[i])
        i = 0
        for val in temp2:
            nums[i] = val
            i += 1
        for val in temp1:
            nums[i] = val
            i += 1

        