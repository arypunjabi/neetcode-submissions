class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 2:
            return max(nums[0],nums[1])
        if n == 1:
            return nums[0]
        
        max2Prev = nums[0]
        max1Prev = max(nums[1],nums[0])

        for i in range(2,n):
            temp = max1Prev
            max1Prev = max(max2Prev + nums[i], max1Prev)
            max2Prev = temp
        
        return max1Prev