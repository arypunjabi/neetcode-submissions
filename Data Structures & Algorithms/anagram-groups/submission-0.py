class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myHash = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in myHash:
                myHash[key].append(s)
            else:
                myHash[key] = [s]
        return list(myHash.values())
            
