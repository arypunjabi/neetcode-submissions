class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefixProd = 1
        suffixProd = 1

        for i in range(1, len(nums)):
            prefixProd = prefixProd * nums[i-1]
            output[i] = prefixProd
        
        for i in range(len(nums)-2, -1, -1):
            suffixProd = suffixProd * nums[i+1]
            output[i] = suffixProd * output[i]

        return output