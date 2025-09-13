class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
    # edge case
        if n==1:
            return nums[0]
        nums.sort()
        i=0
        while i<n-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2
        return nums[-1]