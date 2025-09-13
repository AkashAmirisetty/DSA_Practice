class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        # Edge case
        if n<=2:
            return True
        drop=0
        for i in range(n-1):
            if nums[i+1]<nums[i]:
                drop+=1
                if drop>1:
                    return False
        if drop==0:
            return True
        if drop==1 and nums[n-1]<=nums[0]:
            return True
        else:
            return False
        
        
                
        