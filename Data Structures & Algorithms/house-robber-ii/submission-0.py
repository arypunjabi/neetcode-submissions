class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for house in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + house)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))