class Solution:
    def lowerbound(self, arr, n,x):
        low=0
        high=n-1
        ans=n
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    def rowWithMax1s(self, mat):
        index=-1
        max_count=0
        n=len(mat)
        m=len(mat[0])
        # for i in range(n):
        #     row_count=0
        #     for j in range(m):
        #         row_count+=mat[i][j]
        #     if row_count>max_count:
        #         max_count=row_count
        #         index=i 
        # return index
        for i in range(n):
            row_count= m-self.lowerbound(mat[i],m,1)
            if row_count>max_count:
                max_count=row_count
                index=i 
        return index

    
            

        
       