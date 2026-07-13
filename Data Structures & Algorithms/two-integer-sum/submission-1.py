class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for x in range(len(nums)):
                if ((nums[i] + nums[x]) == target) and (i != x):
                    break
            if ((nums[i] + nums[x]) == target) and (i != x):
                break
        return [i,x]