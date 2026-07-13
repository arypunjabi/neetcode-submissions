class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        L = 0
        length = 0

        for R in range (len(s)):
            if s[R] in window:
                L = max(L, window[s[R]] + 1)
            window[s[R]] = R
            length = max(length, R-L+1)
        return length