class Solution:
    def largestDigit(self, n):
        largest=0
        while n>0:
            last =n%10
            if last>largest:
                largest=last
            n=n//10
        return largest