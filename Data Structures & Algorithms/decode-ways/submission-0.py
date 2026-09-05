class Solution:
    def numDecodings(self, s: str) -> int:
        numWays = [0] * len(s)

        for i in range(len(s)):
            # choice 1
            if i == 0:
                if s[0] != '0':
                    numWays[0] = 1
            else:
                if s[i] != '0':
                    numWays[i] += numWays[i-1]
            
            # choice 2
            if i > 0:
                val = int(s[i - 1] + s[i])
                if 10 <= val <= 26:
                    if i == 1:
                        numWays[i] += 1
                    else:
                        numWays[i] += numWays[i-2]
    
        return numWays[len(s) - 1]