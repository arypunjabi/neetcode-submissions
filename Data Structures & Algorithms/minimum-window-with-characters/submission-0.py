class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1
        
        countS = {}
        l = 0

        have = 0
        need = len(countT)

        bestStart = 0
        bestLen = float("inf")


        for r in range(len(s)):
            if s[r] in countT:
                if s[r] in countS:
                    countS[s[r]] += 1
                    if countS[s[r]] == countT[s[r]]:
                        have += 1
                else:
                    countS[s[r]] = 1
                    if countS[s[r]] == countT[s[r]]:
                        have += 1
            
            while have == need:
                currLen = r - l + 1
                if currLen < bestLen:
                    bestLen = currLen
                    bestStart = l
                
                charLoss = s[l]
                l += 1
                if charLoss in countT:
                    countS[charLoss] -= 1
                    if countS[charLoss] < countT[charLoss]:
                        have -= 1
        
        return s[bestStart: bestLen + bestStart] if bestLen != float("inf") else ""
                    

            
            
