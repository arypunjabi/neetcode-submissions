class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for n in strs:
            encodedString = encodedString + str(len(n)) + "#" + n + "#"
        return encodedString

    def decode(self, s: str) -> List[str]:
        myList =[]
        l1 = 0
        wordSize = 0
        wordSizeString =""
        while l1 < len(s):
            if(s[l1] != "#"):
                wordSizeString = wordSizeString + s[l1]
                l1 = l1 + 1
            else:
                l1 = l1 + 1
                wordSize = int(wordSizeString)
                myList.append(s[l1:l1+wordSize])
                l1 = l1 + wordSize + 1
                wordSize = 0
                wordSizeString = ""
        return myList

            

