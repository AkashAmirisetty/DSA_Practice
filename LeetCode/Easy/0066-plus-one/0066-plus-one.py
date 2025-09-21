class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n):
            if digits[n-1-i]<9:
                digits[n-1-i]=digits[n-1-i]+1
                return digits
            else:
                digits[n-1-i]=0 
        return [1]+digits
        