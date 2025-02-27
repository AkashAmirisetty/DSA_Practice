class Solution:    
    def palindromeCheck(self, s):
        return self.fxn(0,len(s)-1,s)
    
    def fxn(self,l,r,s):
        if l>=r:
            return True
        if s[l]!=s[r]:
            return False
        return self.fxn(l+1,r-1,s)

        
        