class Solution:
    def rotateMatrix(self, matrix):
        # n=len(matrix)
        # ans=[[0]*n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         ans[j][n-1-i]=matrix[i][j]
        # for i in range(n):
        #     matrix[i]=ans[i]
        # return matrix
        n=len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]



