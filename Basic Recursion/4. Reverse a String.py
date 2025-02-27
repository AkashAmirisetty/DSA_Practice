class Solution:
    def reverseString(self,s):
        self.fxn(0,len(s)-1,s)
        return s

    def fxn(self,l,r,s):
        if l>=r:
            return
        s[l],s[r]=s[r],s[l]
        self.fxn(l+1,r-1,s)
        
       

