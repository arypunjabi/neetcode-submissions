class DictNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = DictNode()

    def addWord(self, word: str) -> None:
        iterator = self.root

        for c in word:
            if c not in iterator.children:
                iterator.children[c] = DictNode()
            iterator = iterator.children[c]
        iterator.word = True
        

    def search(self, word: str) -> bool:
        iterator = self.root
        return self.iterate(word, 0, iterator)
    
    def iterate(self, word, wordI, iterator):
        if wordI == len(word):
            return iterator.word
        if word[wordI] == ".":
            res = False
            for c in iterator.children:
                res = res or self.iterate(word, wordI + 1, iterator.children[c])
            return res
        if word[wordI] in iterator.children:
            return self.iterate(word, wordI + 1, iterator.children[word[wordI]])
        if word[wordI] not in iterator.children:
            return False


    

        
