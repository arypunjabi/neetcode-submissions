class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sIndex = 0
        tIndex = 0

        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                sIndex = sIndex + 1
                tIndex = tIndex + 1
            else:
                sIndex = sIndex + 1
        
        return len(t)- tIndex