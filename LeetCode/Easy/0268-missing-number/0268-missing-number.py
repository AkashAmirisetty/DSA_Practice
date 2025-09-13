class Solution:
    def missingNumber(self, nums: List[int]) -> int:
# Approach 1
        # n=len(nums)
        # sum1=(n*(n+1))//2
        # sum2=sum(nums)
        # missing=sum1-sum2
        # return missing

# Approach 2
        nums.sort()
        n=len(nums)
        if nums[0]!=0:
            return 0
        i=0
        j=1
        while j<n:
            if nums[j]==nums[i]+1:
                i=i+1
                j=j+1
            else:
                return nums[i]+1
        return n



        