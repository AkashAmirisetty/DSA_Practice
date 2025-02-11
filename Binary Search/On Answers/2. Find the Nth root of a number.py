class Solution:
    # Linear search approach
    def power(self,j, k): #Power function
        return j**k

    def NthRoot(self, n, m):

        # for i in range(m):
        #     if self.power(i,n)==m:
        #         return i 
        #     elif self.power(i,n)>m:
        #         break
        # return -1
        low=1
        high=m
        while low<=high:
            mid=(low+high)//2
            mid_power= self.power(mid,n)
            if mid_power==m:
                return mid
            elif mid_power>m:
                high=mid-1
            else:
                low=mid+1
        return -1





    



        
        
      