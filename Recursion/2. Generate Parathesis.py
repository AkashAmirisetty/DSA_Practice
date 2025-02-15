class Solution:
    def generateParenthesis(self, n):
        ans=[]
        self.function(0,0,ans,n,"")
        return ans
    def function(self, o:int, c:int, ans:list, n:int, curr:str):
        if o>n:
            return
        if o+c==2*n and o==c:
            ans.append(curr)
            return
        if o<n:
            self.function(o+1,c,ans,n,curr+'(')
        if o>c:
            self.function(o,c+1,ans,n,curr+')')
        
        


       