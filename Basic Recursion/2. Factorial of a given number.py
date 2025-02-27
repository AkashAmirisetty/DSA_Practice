class Solution:
    def factorial(self, n):
        #Your code goes here
        if n==0:
            return 1
        fact=n*self.factorial(n-1)
        return fact
