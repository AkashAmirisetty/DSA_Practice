class Solution:
    def generateRow(self, row):
        ans=1
        ansRow=[1]
        for i in range(1,row):
            ans=ans*(row-i)
            ans=ans//i 
            ansRow.append(ans)
        return ansRow
    def pascalTriangle(self, numRows):
        pascalTriangle=[]
        for row in range(1,numRows+1):
            pascalTriangle.append(self.generateRow(row))
        return pascalTriangle
