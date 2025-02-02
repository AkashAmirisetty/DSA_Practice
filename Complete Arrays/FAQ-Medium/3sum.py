class Solution:
    def threeSum(self, nums):
        # Time limit exceeds
        # n=len(nums)
        # triplet=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 temp.sort()
        #                 triplet.add(tuple(temp))
        # ans=[list(triplet) for triplet in triplet]
        # return ans  
# Better Approach
        # triplet_set=set()
        # n=len(nums)
        # for i in range(n):
        #     hashset=set()
        #     for j in range(i+1,n):
        #         k=-(nums[i]+nums[j])
        #         if k in hashset:
        #             temp=[nums[i],nums[j],k]
        #             temp.sort()
        #             triplet_set.add(tuple(temp))
        #         hashset.add(nums[j])
        # ans=[list(triplet) for triplet in triplet_set]
        # return ans
        # OPTIMAL APPROACH
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                sum_value=nums[i]+nums[j]+nums[k]
                if sum_value<0:
                    j+=1
                elif sum_value>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
        return ans

        
