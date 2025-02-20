class Solution:
    def subsetsWithDup(self, nums):
        ans = []
        arr = []
        nums.sort() 
        self.func(0, arr, nums, ans)
        return ans

    def func(self, ind, arr, nums, ans):
        ans.append(arr[:])  
        
        for j in range(ind, len(nums)):
            if j > ind and nums[j] == nums[j - 1]:  
                continue
            
            arr.append(nums[j])  
            self.func(j + 1, arr, nums, ans)  
            arr.pop() 