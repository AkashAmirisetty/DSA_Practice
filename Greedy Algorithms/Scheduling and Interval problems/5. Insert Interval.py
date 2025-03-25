class Solution:
    def insertNewInterval(self, Intervals, newInterval):
        #your code goes here
        n=len(Intervals)
        res=[]
        i=0
        # Left half
        while (i<n and Intervals[i][1]< newInterval[0]):
            res.append(Intervals[i])
            i+=1
        # Merged half
        while (i<n and Intervals[i][0]<=newInterval[1]):
            newInterval[0]=min(Intervals[i][0], newInterval[0])
            newInterval[1]=max(Intervals[i][1], newInterval[1])
            i+=1
        res.append(newInterval)
        # Right half
        while (i<n):
            res.append(Intervals[i])
            i+=1
        return res

        
