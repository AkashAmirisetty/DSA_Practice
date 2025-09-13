class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# Approach 1
        # n=len(nums)
        # unique=set(nums)
        # sorted_unique=sorted(unique)
        # for i in range(len(sorted_unique)):
        #     nums[i]=sorted_unique[i]
        # return len(sorted_unique)

# Approach 2
        i=0
        n=len(nums)
        for j in range(1,n):
            if nums[j]!=nums[i]:
                i+=1 #Increment then overwite it
                nums[i]=nums[j] #overwrite
        return i+1



        

        