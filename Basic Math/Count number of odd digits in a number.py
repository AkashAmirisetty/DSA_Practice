class Solution:
    def countOddDigit(self, n):
        countodd=0
        while n>0:
            last = n % 10
            if (last % 2) == 1:
                countodd+=1
            n=n//10
        return countodd