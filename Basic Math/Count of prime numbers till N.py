class Solution:
    def primeUptoN(self, n):
        def isPrime(n):
            if n==1:
                return False
            for i in range(2, int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        count=0
        for i in range(2, n+1):
            if isPrime(i):
                count+=1
        return count