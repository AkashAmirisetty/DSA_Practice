class Solution:
    def reverseArray(self, nums, start, end):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
    def rotateArray(self, nums, k):
        n=len(nums)
        k=k%n
        self.reverseArray(nums,0,k-1)
        self.reverseArray(nums, k, n-1)
        self.reverseArray(nums, 0,n-1)
def printArray(nums):
    for val in nums:
        print(val, end=" ")
    print()
