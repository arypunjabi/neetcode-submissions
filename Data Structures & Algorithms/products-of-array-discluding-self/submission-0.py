class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        totalProd = 1
        zero = 0
        
        for i in nums:
            if i == 0:
                zero += 1
            else:
                totalProd *= i
        
        for x in range(len(nums)):
            if zero == 0:
                output[x] = totalProd//nums[x]
            elif zero == 1:
                if nums[x] == 0:
                    output[x] = totalProd
                else:
                    output[x] = 0
            else:
                output[x] = 0
        
        return output
