class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestHeight = 0
        L = 0
        R = len(heights)-1

        while L < R:
            currHeight = (R-L) * min(heights[L], heights[R])
            largestHeight = max(largestHeight, currHeight)

            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return largestHeight