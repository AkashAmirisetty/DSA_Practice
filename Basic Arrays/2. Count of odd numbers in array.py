class Solution:
	def countOdd(self, arr, n):
		count=0
		for i in arr:
			if i%2==1:
				count+=1
		return count

