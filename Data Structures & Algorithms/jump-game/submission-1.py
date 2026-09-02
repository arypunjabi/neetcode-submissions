class Solution:
    def canJump(self, nums: List[int]) -> bool:

        visit = set()
        
        def jump(currI):
            if currI in visit:
                return False
            visit.add(currI)
            if currI == len(nums) - 1:
                return True
            if currI >= len(nums):
                return False
            
            res = False
            for i in range(1, nums[currI] + 1):
                res = res or jump(currI + i)

            return res
        
        return jump(0)