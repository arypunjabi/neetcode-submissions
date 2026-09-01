class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqHash = {}
        maxFreq = 0
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in freqHash:
                freqHash[s[r]] = freqHash[s[r]] + 1
            else:
                freqHash[s[r]] = 1
            maxFreq = max(maxFreq, freqHash[s[r]])

            while (r - l + 1) - maxFreq > k:
                freqHash[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res
