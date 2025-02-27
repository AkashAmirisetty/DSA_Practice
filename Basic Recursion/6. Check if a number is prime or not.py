class Solution:
    def checkPrime(self, num):
        return self.fxn(2,num)
        #your code goes here
        # Iterative method
        # for i in range(2,num):
        #     if num%i==0:
        #         return False
        # return True
        # Recursive Method
    def fxn(self,i,num):
        if num<2:
            return False
        if i>=num**0.5:
            return True
        if num%i==0:
            return False
        return self.fxn(i+1,num)

