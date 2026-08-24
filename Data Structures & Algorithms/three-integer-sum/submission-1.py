class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortNums = sorted(nums)

        for a in range(len(sortNums)):
            if a > 0 and sortNums[a] == sortNums[a-1]:
                continue
            L = a + 1
            R = len(sortNums) - 1
            while L < R:
                if sortNums[L] + sortNums[R] + sortNums[a] == 0:
                    res.append([sortNums[L], sortNums[R], sortNums[a]])
                    L = L + 1
                    while sortNums[L] == sortNums[L-1] and L < R:
                        L = L + 1
                elif sortNums[L] + sortNums[R] + sortNums[a] > 0:
                    R = R - 1
                else:
                    L = L + 1
        
        return res


