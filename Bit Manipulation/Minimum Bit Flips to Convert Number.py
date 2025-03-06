class Solution:
    def minBitsFlip(self, start, goal):
# ------------------MY APPROACH--------------------------------

    #     start=self.decitobinary(start)
    #     goal=self.decitobinary(goal)
    #     max_len = max(len(start), len(goal))
    #     # zfill() is a built-in string method that adds zeroes to beginning
    #     start = start.zfill(max_len) #to add zeroes to the starting if it has less number of places
    #     goal = goal.zfill(max_len) #to add zeroes to the starting if it has less number of places
    #     count=0
    #     for i in range(0,max_len):
    #         if start[i]!=goal[i]:
    #             count+=1
    #     return count
    # def decitobinary(self,n):
    #     if n==0:
    #         return "0"
    #     res=""
    #     while n>0:
    #         if n%2==1:
    #             res="1"+res
    #         else:
    #             res="0"+res
    #         n=n//2
    #     return res

# --------------OPTIMAL(STRIVER's)----------------------------
    
        