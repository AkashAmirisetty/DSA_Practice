class Solution:
    def twoSum(self, nums, target):
        # MY APPROACH (TIME LIMIT EXCEEDS)
        n=len(nums)
        # i=0
        # j=i+1
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #          return [i,j]
        # return []
        hashmap={}
        for i in range(n):
            num=nums[i]
            more_need=target-num
            if more_need in hashmap:
                return [hashmap[more_need],i]
            hashmap[num]=i 
        return []

        