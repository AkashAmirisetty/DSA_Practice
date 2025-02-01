class Solution:
    def isPalindrome(self, n):
        duplicate=n
        rev=0
        while n>0:
            last=n%10
            rev=rev*10+last
            n=n//10
        if rev==duplicate:
            return True
        return False