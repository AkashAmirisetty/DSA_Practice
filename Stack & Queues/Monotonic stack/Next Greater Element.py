# Given an array arr of size n containing elements, find the next greater element for each element in the array in the order of their appearance.
# Examples:
# Input: arr = [1, 3, 2, 4]

# Output: [3, 4, 4, -1]

# Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1, since it does not exist.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------



class Solution:
    def nextLargerElement(self, arr):
        # Brute-Force
        # n=len(arr)
        # ans=[-1]*n 
        # for i in range(n):
        #     currele=arr[i]
        #     for j in range(i+1,n):
        #         if arr[j]>currele:
        #             ans[i]=arr[j]
        #             break
        # return ans

        # Optimal using stack
        n=len(arr)
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            currele=arr[i]
            while stack and stack[-1]<=currele:
                stack.pop()
            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(currele)
        return ans






   