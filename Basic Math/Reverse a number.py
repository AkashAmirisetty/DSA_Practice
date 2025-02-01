class Solution:
    def reverseNumber(self, n):
        rev_num=0
        while n>0:
            lastdigit=n%10
            rev_num=rev_num*10+lastdigit
            n=n//10
        return rev_num



