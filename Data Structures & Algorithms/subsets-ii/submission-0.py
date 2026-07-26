class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        newNums = sorted(nums)
        subsets = []
        currSet = []

        self.helper(0, newNums, currSet, subsets)
        return subsets
    
    def helper(self, i, newNums, currSet, subsets):
        if i >= len(newNums):
            subsets.append(currSet.copy())
            return
        
        #if choose
        currSet.append(newNums[i])
        self.helper(i + 1, newNums, currSet, subsets)
        currSet.pop()

        #if not choose
        while i + 1 < len(newNums) and newNums[i] == newNums[i + 1]:
            i = i + 1
        self.helper(i + 1, newNums, currSet, subsets)
