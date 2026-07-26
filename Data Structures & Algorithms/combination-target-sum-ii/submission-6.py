class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        newNums = sorted(candidates)
        subsets = []
        currSet = []
        self.helper(0, newNums, subsets, currSet, target)
        return subsets
    
    def helper(self, i, newNums, subsets, currSet, target):
        if sum(currSet) > target:
            return
        elif sum(currSet) == target:
            subsets.append(currSet.copy())
            return
        elif i >= len(newNums):
            return
        
        #Plus Then Move on
        currSet.append(newNums[i])
        self.helper(i + 1, newNums, subsets, currSet, target)
        currSet.pop()

        #Ignore and move on
        while i + 1 < len(newNums) and newNums[i] == newNums[i+1]:
            i = i + 1
        self.helper(i + 1, newNums, subsets, currSet, target)
