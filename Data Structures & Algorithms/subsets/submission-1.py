class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSubset = []
        self.helper(0, nums, currSubset, subsets)

        return subsets
        
    def helper(self, i, nums, currSubset, subsets):
        if i >= len(nums):
            subsets.append(currSubset.copy())
            return
        
        #include
        currSubset.append(nums[i])
        self.helper(i+1, nums, currSubset, subsets)
        currSubset.pop()

        #don't include
        self.helper(i+1, nums, currSubset, subsets)