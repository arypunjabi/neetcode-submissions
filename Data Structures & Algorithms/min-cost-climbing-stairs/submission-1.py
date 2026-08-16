class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        prev2Min = cost[0]
        prev1Min = cost[1]

        for i in range(2, n):
            temp = prev1Min
            prev1Min = min(prev2Min, prev1Min) + cost[i]
            prev2Min = temp

        return min(prev1Min, prev2Min)
