class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        k = 0
        while i < len(chars):
            tempS = chars[i]
            numOccur = 0
            while i < len(chars) and chars[i] == tempS:
                numOccur += 1
                i += 1
            if numOccur > 1:
                tempS = tempS + str(numOccur)
                for c in tempS:
                    chars[k] = c
                    k += 1
            else:
                chars[k] = tempS
                k += 1
        
        return k

