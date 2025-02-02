class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                count+=1
                max_count= max(count, max_count)
                # i+=1
            elif nums[i]!=1:
                count=0
        return max_count
            

            
        