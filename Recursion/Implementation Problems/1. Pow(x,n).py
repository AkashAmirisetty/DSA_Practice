class Solution:    
    # def myPow(self, x, n):
        #your code goes here
        # return x**n
        # ans=1
        # if n<0:
        #     x=1/x
        #     n=(-1)*n 
        # for i in range(n): #Repeats n times
        #     ans=ans*x   #multiplied by x until the for loop runs
        # return ans
        # Iterrative method
        # ans=1
        # if n<0:
        #     x=1/x
        #     n=(-1)*n 
        # while n>0:
        #     if n%2==1: #odd condition
        #         ans=ans*x
        #         n=n-1
        #     else:
        #         x=x*x
        #         n=n/2
        # return ans
        # Recursive method
        def power(self, x,n):
            if n==0:
                return 1
            if n==1:
                return x
            if n%2==0:
                return self.power(x*x,n//2)
            else:
                return x*self.power(x,n-1)

        def myPow(self, x, n):
            if n<0:
                return self.power(1/x,-n)
            else:
                return self.power(x,n)

        
        
            
