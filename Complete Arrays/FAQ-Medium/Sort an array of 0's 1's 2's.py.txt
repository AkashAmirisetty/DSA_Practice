class Solution:
    def sortZeroOneTwo(self, nums):
        # Brute Force (T.C=nlogn)
        # n=len(nums)
        # return nums.sort()
        n=len(nums)
        # zeroes=0
        # ones=0
        # twos=0
        # for num in nums:
        #     if num==0:
        #         zeroes+=1
        #     elif num==1:
        #         ones+=1
        #     else:
        #         twos+=1
        # for i in range(zeroes):
        #     nums[i]=0
        # for j in range(zeroes,zeroes+ones):
        #     nums[j]=1
        # for k in range(zeroes+ones, n):
        #     nums[k]=2
        low=0
        mid=0
        high=n-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
                
            
