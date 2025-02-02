class Solution:
    def unionArray(self, nums1, nums2):
        # MY APPROACH
        # temp=list(set(nums1+nums2))
        # temp=sorted(temp)
        # return temp
        # Optimal
        union=[]
        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                if not union or union[-1]!= nums1[i]: 
                # If the element is not present in the arr or previous element that is stored
                    union.append(nums1[i])
                i+=1
            else:
            # Condition if nums1[j]<=nums[i]
                if not union or union[-1]!=nums2[j]:
                    union.append(nums2[j])
                j+=1
            # Condition for left out elements
        while i<n:
            if not union or union[-1]!=nums1[i]:
                union.append(nums1[i])
            i+=1
        while j<m:
            if not union or union[-1]!=nums2[j]:
                union.append(nums2[j])
            j+=1
        return union





