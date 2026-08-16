class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        uniquePaths = [[0] * n for _ in range(m)]

        for i in range(m):
            uniquePaths[i][0] = 1
        
        for i in range(n):
            uniquePaths[0][i] = 1

        for r in range(1,m):
            for c in range(1,n):
                uniquePaths[r][c] = uniquePaths[r][c-1] + uniquePaths[r-1][c]

        return uniquePaths[m-1][n-1]