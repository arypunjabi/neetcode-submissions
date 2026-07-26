class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        currSet = []

        self.helper(0, nums, subsets, currSet, target)
        return subsets

    def helper(self, i, nums, subsets, currSet, target):
        if i >= len(nums):
            return
        if sum(currSet) > target:
            return
        if sum(currSet) == target:
            subsets.append(currSet.copy())
            return

            
        # Plus and stay
        currSet.append(nums[i])
        self.helper(i, nums, subsets, currSet, target)
        currSet.pop()

        # Ignore and move on
        self.helper(i + 1, nums, subsets, currSet, target)