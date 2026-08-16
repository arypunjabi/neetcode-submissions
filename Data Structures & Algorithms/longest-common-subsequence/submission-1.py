class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        longSub = [[0] * (n1+1) for _ in range(n2+1)]

        for r in range(1,n2+1):
            for c in range(1,n1+1):
                if text1[c-1] == text2[r-1]:
                    longSub[r][c] = longSub[r-1][c-1] + 1
                else:
                    longSub[r][c] = max(longSub[r-1][c], longSub[r][c-1])
        
        return longSub[n2][n1]