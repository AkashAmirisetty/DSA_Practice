class Solution:
    def fourSum(self, nums, target):
        # n=len(nums)
        # ans=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for l in range(k+1,n):
        #                 sum_value=nums[i]+nums[j]+nums[k]+nums[l]
        #                 if sum_value==target:
        #                     temp=[nums[i],nums[j],nums[k],nums[l]]
        #                     temp.sort()
        #                     ans.add(tuple(temp))
        # return list(ans)

        # ans = []
        # n = len(nums)
        # unique_set = set()
    
        # nums.sort() 
    
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         hashset = set()
        #         for k in range(j + 1, n):
        #             sum_val = nums[i] + nums[j] + nums[k]
        #             l = target - sum_val
        #             if l in hashset:
        #                 temp = [nums[i], nums[j], nums[k], l]
        #                 temp.sort()
        #                 unique_set.add(tuple(temp))
        #             hashset.add(nums[k])
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue      
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1               
                while k < l:
                    sum_val = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_val == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)                        
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sum_val < target:
                        k += 1
                    else:
                        l -= 1
        return ans
                        
                    


        







        