class Solution:
    def maxMeetings(self, start, end):
        #your code goes here
        n=len(start)
        meetings=[]
        cnt=1
        for i in range(n):
            meetings.append((start[i],end[i]))
        meetings.sort(key=lambda x: x[1])
        freeTime=meetings[0][1]  #Free time will be first meeting end
        for i in range(1,n):
            if meetings[i][0]>freeTime:
                freeTime=meetings[i][1]
                cnt+=1
        return cnt


