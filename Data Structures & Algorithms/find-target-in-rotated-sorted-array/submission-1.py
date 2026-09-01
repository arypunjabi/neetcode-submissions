class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        index = -1

        while L <= R:
            m = (L + R) // 2
            if nums[m] == target:
                index = m
                break

            if nums[L] <= nums[m] and nums[m] <= nums[R]:
                # already sorted
                if nums[m] < target:
                    L = m + 1
                elif nums[m] > target:
                    R = m - 1
            elif nums[L] <= nums[m]:
                #left side is sorted
                if target < nums[m] and target >= nums[L]:
                    R = m - 1
                else:
                    L = m + 1
            elif nums[m] <= nums[R]:
                #right side is sorted
                if target > nums[m] and target <= nums[R]:
                    L = m + 1
                else:
                    R = m - 1
        return index