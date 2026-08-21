class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        hashM = {}
        for i in strings:
            diffArr = []
            if len(i) == 1:
                diffArr = [27]
            else:
                for c in range(1,len(i)):
                    diffArr.append((ord(i[c])-ord(i[c-1])) % 26)
            
            key = tuple(diffArr)
            if key in hashM:
                hashM[key].append(i)
            else:
                hashM[key] = [i]
        
        return list(hashM.values())


