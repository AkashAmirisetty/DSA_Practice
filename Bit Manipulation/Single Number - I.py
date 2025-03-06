class Solution:
    def singleNumber(self, nums):
        result=0
        for num in nums:
            result=result^num
        return result
    # def singleNumber(self,nums):
    # 2Pointer approach (MY approach not working)
        # nums.sort()
        # n=len(nums)
        # if n==1:
        #     return nums[0]
        # a=0
        # while a<n-1:
        #     if nums[a]==nums[a+1]:
        #         a+=2
        #     else:
        #         return nums[a]

        