class Solution:
    def partition(self,arr,low,high):
        pivot=arr[low]
        i=low
        j=high
        while(i<j):
            while arr[i]<=pivot and i<=high-1:
                i+=1
            while arr[j]>pivot and j>= low+1:
                j-=1
            if i<j:
                arr[i],arr[j]= arr[j], arr[i]
        arr[low],arr[j]= arr[j], arr[low]
        return j
    def quicksorter(self, arr, low, high):
        if low<high:
            partition_index=self.partition(arr, low, high)
            self.quicksorter(arr, low, partition_index-1)
            self.quicksorter(arr, partition_index+1, high)

    def quickSort(self, nums):
        n=len(nums)
        self.quicksorter(nums, 0, n-1)
        return nums