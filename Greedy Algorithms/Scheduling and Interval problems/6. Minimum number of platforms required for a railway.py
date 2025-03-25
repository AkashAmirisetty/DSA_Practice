class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        n=len(Arrival)
        Arrival.sort()
        i=0
        Departure.sort()
        j=0
        cnt=0
        maxcnt=0
        while i<n and j<n:
            if Arrival[i]<=Departure[j]:
                cnt+=1
                i+=1
            else:
                cnt-=1
                j+=1
            maxcnt=max(maxcnt,cnt)
        return maxcnt




       