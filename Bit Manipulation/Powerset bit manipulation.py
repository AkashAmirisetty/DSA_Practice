class Solution:
    def powerSet(self, nums):
        #your code goes here
        n=len(nums)
        subsets=(1<<n)
        ans=[]
        for num in range(0,subsets):
            lis=[]
            for i in range(0,n):
                if num & (1<<i):
                    lis.append(nums[i])
            ans.append(lis)
        return ans
