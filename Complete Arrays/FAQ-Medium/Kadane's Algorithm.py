class Solution:
    def maxSubArray(self, nums):
        n=len(nums)
        # maxi=float('-inf')
        # for i in range(n):
        #     summ=0
        #     for j in range(i,n):
        #         summ+=nums[j]
        #         maxi=max(maxi,summ)
        # return maxi
        maxi=float('-inf')
        summ=0
        for i in range(n):
            summ+=nums[i]
            if summ>maxi:
                maxi=summ
            if summ<0:
                summ=0
        return maxi




        