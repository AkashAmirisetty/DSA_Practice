import math
class Solution:
    def summ(self, nums, j):
        n=len(nums)
        sum_val=0
        for num in nums:
            sum_val+=math.ceil(num/j)
        return sum_val
        
    def smallestDivisor(self, nums, limit):
        # My Brute Approach
        n=len(nums)
        # i=1
        # while True:
        #     total=0
        #     for ele in nums:
        #         total+=math.ceil(ele/i)
        #     if total<=limit:
        #         return i 
        #     else:
        #         i+=1
        # maxi=max(nums)
        # for divisor in range(1,maxi+1):
        #     summ=0
        #     for i in range(n):
        #         summ=summ+math.ceil(nums[i]/divisor) #Ceil used for rounding off the number (if 4.5-->5)
        #     if summ<=limit:
        #         return divisor
        # return -1
        ans=-1
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            if self.summ(nums, mid)<=limit:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
            
            

        