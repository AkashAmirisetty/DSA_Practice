class Solution:
    def divisors(self, n):
        result=[]
        for i in range(1,int(n)+1):
            if n%i==0:
                result.append(i)
        return result 