class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = end // 2
        localMin = 1001

        while start < end:
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
            mid = (start + end) // 2
        return nums[mid]
