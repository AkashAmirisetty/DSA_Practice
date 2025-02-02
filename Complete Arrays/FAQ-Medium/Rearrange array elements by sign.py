class Solution:
    def rearrangeArray(self, nums):
        n=len(nums)
        # pos=[]
        # neg=[]
        # for num in nums:
        #     if num>0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)
        # for i in range(n//2):
        #     nums[2*i]=pos[i]
        #     nums[2*i+1]=neg[i]
        # return nums
        ans=[0]*n
        posindex=0
        negindex=1
        for i in range(n):
            if nums[i]<0:
                ans[negindex]=nums[i]
                negindex+=2
            else:
                ans[posindex]=nums[i]
                posindex+=2
        return ans


        