class Solution:
    def floorSqrt(self, n: int) -> int:
        # return int(n**0.5) #Simple approach

        # Linear search approach (TC: O(N); SC: O(1))
        # ans=1
        # for i in range(n+1):
        #     if i*i<=n:
        #         ans=i
        #     else:
        #         break   
        # return ans     

        # Binary search approach
        ans=1
        low=1
        high=n 
        if n==0:
            ans=0
        while low<=high:
            mid=(low+high)//2
            if (mid*mid<=n):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        
