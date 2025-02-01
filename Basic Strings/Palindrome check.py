class Solution: 
    def reverseString(self, s):
        #your code goes here
        leng=len(s)
        left=0
        right=leng-1
        while (left<right):
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

        