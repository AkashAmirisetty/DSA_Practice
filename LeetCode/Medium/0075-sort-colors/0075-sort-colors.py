class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Extreme Brute 
        # nums.sort()
        cnt0=0
        cnt1=0
        cnt2=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                cnt0+=1
            elif nums[i]==1:
                cnt1+=1
            else:
                cnt2+=1
        for i in range(cnt0):
            nums[i]=0
        for i in range(cnt0,cnt0+cnt1):
            nums[i]=1
        for i in range(cnt0+cnt1,n):
            nums[i]=2
            
        