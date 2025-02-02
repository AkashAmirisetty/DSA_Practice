class Solution:
    def leaders(self, nums):
        # ans=[]
        # n=len(nums)
        # for i in range(n):
        #     leader=True
        #     for j in range(i+1,n):
        #         if nums[i]<=nums[j]:
        #             leader=False
        #             break
        #     if leader==True:
        #         ans.append(nums[i])
        # return ans
        ans=[]
        if not nums:
            return ans
        maximum=nums[-1]
        n=len(nums)
        ans.append(nums[-1])
        for i in range(n-2, -1, -1):
            if nums[i]>maximum:
                ans.append(nums[i])
                maximum=nums[i]
        ans.reverse()
        return ans

