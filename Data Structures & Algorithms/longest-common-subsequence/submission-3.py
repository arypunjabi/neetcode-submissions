class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prevLongSub = [0] * (len(text1) + 1)
        currLongSub = [0] * (len(text1) + 1)
        for r in range(1,len(text2) + 1):
            for c in range(1,len(text1) + 1):
                if text1[c-1] == text2[r-1]:
                    currLongSub[c] = prevLongSub[c-1] + 1
                else:
                    currLongSub[c] = max(prevLongSub[c], currLongSub[c-1])
            prevLongSub = currLongSub
            currLongSub = [0] * (len(text1) + 1)
        return prevLongSub[len(text1)]