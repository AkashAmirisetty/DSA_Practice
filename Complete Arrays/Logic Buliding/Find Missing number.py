class Solution:
    def missingNumber(self, nums):
        # MY APPROACH
        # n=len(nums)
        # numbers= list(range(n+1))
        # sorted_nums=sorted(nums)
        # for i in range(n+1):
        #     if i>=n or sorted_nums[i]!=numbers[i]:
        #         return numbers[i]
        n=len(nums)
        sum1=(n*(n+1))//2
        sum2=0
        for i in range(n):
            sum2+=nums[i]
        return (sum1-sum2)




        