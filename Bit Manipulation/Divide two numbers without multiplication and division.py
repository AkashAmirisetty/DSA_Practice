class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #your code goes here
        # Worst possible solution:(
        # if divisor<0:
        #     divisor=divisor-1
        # return dividend//divisor
# --------Brute force solution----------(Time linit exceed because of 2^31-1)
        # summ=0
        # cnt=0
        # while (summ+divisor<=dividend):
        #     cnt+=1
        #     summ=summ+divisor
        # return summ
# ------------Optimal Solution--------------
        if dividend==divisor:
            return 1
        sign=True
        if dividend>=0 and divisor<0:
            sign=False
        elif dividend<0 and divisor>0:
            sign=False
        n=abs(dividend)
        d=abs(divisor)
        ans=0
        while n>=d:
            cnt=0
            while n>=(d<<(cnt+1)): #n>=d*2^(cnt+1) this can be written as left shift operator
                cnt+=1
            ans+=(1<<cnt)
            n=n-(d*(1<<cnt))
        if ans>=2**31 and sign==True:
            return (2**31)-1
        if ans>=2**31 and sign==False:
            return (-2**31)
        return ans if sign==True else (-1*ans)




