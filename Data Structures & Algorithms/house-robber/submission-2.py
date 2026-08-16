class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 2:
            return max(nums[0],nums[1])
        if n == 1:
            return nums[0]
        
        maxMon = [0] * (n + 1)
        maxMon[0] = nums[0]
        maxMon[1] = max(nums[1],nums[0])

        for i in range(2,n):
            maxMon[i] = max(maxMon[i-2] + nums[i], maxMon[i-1])
        
        return maxMon[n-1]