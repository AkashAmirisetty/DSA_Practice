class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIndex=0
        negIndex=1
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            if nums[i]>0:
                ans[posIndex]=nums[i]
                posIndex+=2
            else:
                ans[negIndex]=nums[i]
                negIndex+=2
        return ans
        