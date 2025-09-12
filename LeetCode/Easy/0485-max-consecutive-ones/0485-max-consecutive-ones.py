class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        one_cnt=0
        max_cnt=0
        for i in range(n):
            if nums[i]==1:
                one_cnt+=1
            else:
                one_cnt=0
            max_cnt=max(one_cnt,max_cnt)
        return max_cnt

        