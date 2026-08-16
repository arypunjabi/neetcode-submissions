class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path2 = [1] * n
        path1 = [0] * n

        path1[0] = 1

        for r in range(1,m):
            for c in range(1,n):
                path1[c] = path1[c-1] + path2[c]
            path2 = path1
            path1 = [0] * n
            path1[0] = 1

        return path2[n-1]