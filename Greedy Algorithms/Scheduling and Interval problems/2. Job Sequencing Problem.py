class Solution:
    def JobScheduling(self, Jobs):
        #your code goes here
        profit=0
        cnt=0
        n=len(Jobs)
        Jobs.sort(key=lambda x:x[2], reverse=True)
        hashmap=[-1]*n
        for i in range(n):
            for j in range(Jobs[i][1]-1,-1,-1):
                if hashmap[j]==-1:
                    cnt+=1
                    hashmap[j]=Jobs[i][0]
                    profit+=Jobs[i][2]
                    break
        return [cnt, profit]


