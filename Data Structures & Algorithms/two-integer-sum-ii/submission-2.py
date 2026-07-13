class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            if (numbers[L] + numbers[R]) > target:
                R = R - 1
            elif (numbers[L] + numbers[R]) < target:
                L = L + 1
            else:
                return [L + 1, R + 1]
        return -1