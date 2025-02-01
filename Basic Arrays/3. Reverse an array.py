class Solution:
    def reverse(self, arr, n):
        left=0
        right=n-1
        while (left<right):
            arr[left], arr[right]=arr[right], arr[left]
            left=left+1
            right=right-1


