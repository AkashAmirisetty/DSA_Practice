class Solution:
    def MaximumNonOverlappingIntervals(self, Intervals):
        #your code goes here
        n=len(Intervals)
        Intervals.sort(key=lambda x: x[1])
        count=1
        lastEndtime=Intervals[0][1]
        for i in range(1,n):
            if Intervals[i][0]>=lastEndtime:
                lastEndtime=Intervals[i][1]
                count+=1
        return n-count
        
        