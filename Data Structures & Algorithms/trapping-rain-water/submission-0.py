class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        leftMax = height[L]
        rightMax = height[R]
        totalWaterArea = 0

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(leftMax, height[L])
                totalWaterArea += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(rightMax, height[R])
                totalWaterArea += rightMax - height[R]
        
        return totalWaterArea
            
            