class Solution:    
    def myPow(self, x, n):
        #your code goes here
        # return x**n
        ans=1
        if n<0:
            x=1/x
            n=(-1)*n 
        for i in range(n): #Repeats n times
            ans=ans*x   #multiplied by x until the for loop runs
        return ans