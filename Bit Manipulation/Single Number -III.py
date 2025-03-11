class Solution:   
    def singleNumber(self, nums):
        #your code goes here
        n=len(nums)
        ans=[]
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        for key,value in mpp.items():
            if value==1:
                ans.append(key)
        ans.sort()
        return ans
            
