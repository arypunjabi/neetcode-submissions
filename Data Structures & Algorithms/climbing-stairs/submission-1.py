class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        numTimes = [0] * (n + 1)
        numTimes[1] = 1
        numTimes[2] = 2

        for i in range(3,n + 1):
            numTimes[i] = numTimes[i-1] + numTimes[i-2]
        
        return numTimes[n]