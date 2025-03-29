class Solution:
    def longestNonRepeatingSubstring(self, s):
        # n=len(s)
        # maxlength=0
        # for i in range(n):
        #     hashmap=[0]*256
        #     for j in range(i,n):
        #         if hashmap[ord(s[j])]==1:
        #             break
        #         length=j-i+1
        #         hashmap[ord(s[j])]=1
        #         maxlength=max(maxlength,length)
        # return maxlength
        hashlength=256
        hashmap=[-1]*hashlength
        n=len(s)
        l=0
        r=0
        length=0
        maxlength=0
        while r<n:
            if hashmap[ord(s[r])]!=-1:
                if hashmap[ord(s[r])]>=l:
                    l=hashmap[ord(s[r])]+1
            length=r-l+1
            maxlength=max(length,maxlength)
            hashmap[ord(s[r])]=r
            r+=1
        return maxlength
            



        
        
