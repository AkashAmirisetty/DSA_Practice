class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        n=len(cardScore)
        leftsum=0
        rightsum=0
        maxsum=0
        for i in range(k-1):
            leftsum+=cardScore[i]
            maxsum=leftsum
        rightindex=n-1
        for i in range(k-1,-1,-1):
            leftsum-=cardScore[i]
            rightsum+=cardScore[i]
            rightindex-=1
            maxsum=max(maxsum, leftsum+rightsum)
        return maxsum


        