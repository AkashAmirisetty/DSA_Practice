class Solution:
    def reversal(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.reversal(nums,0,n-1)
        self.reversal(nums,0,k-1)
        self.reversal(nums,k,n-1)



        