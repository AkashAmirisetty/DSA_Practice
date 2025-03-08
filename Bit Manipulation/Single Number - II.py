# Input : nums = [2, 2, 2, 3]
# Output : 3
# Explanation : The integers 3 has appeared only once.
# Input : nums = [1, 0, 3, 0, 1, 1, 3, 3, 10, 0]
# Output : 10
# Explanation : The integers 10 has appeared only once.


class Solution:
    def singleNumber(self, nums):
        #your code goes here
        n=len(nums)
        nums.sort()
        for i in range(1,n,3):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
        return nums[n-1]