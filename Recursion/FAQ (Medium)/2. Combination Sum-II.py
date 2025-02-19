class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  
        self.ans = []
        self.function(0, target, [], candidates)
        return self.ans

    def function(self, index, target, lis, candidates):
        if target == 0:
            self.ans.append(lis[:])  
            return 
        if target < 0 or index == len(candidates):
            return 

        for i in range(index, len(candidates)):  
            if i > index and candidates[i] == candidates[i - 1]:  
                continue  

            lis.append(candidates[i])
            self.function(i + 1, target - candidates[i], lis, candidates)  
            lis.pop()  
