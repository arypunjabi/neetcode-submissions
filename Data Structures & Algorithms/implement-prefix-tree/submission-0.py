class PTreeNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = PTreeNode()

    def insert(self, word: str) -> None:
        iterator = self.root
        for c in word:
            if not(c in iterator.children):
                iterator.children[c] = PTreeNode()
            iterator = iterator.children[c]
        iterator.word = True


    def search(self, word: str) -> bool:
        iterator = self.root
        for c in word:
            if not(c in iterator.children):
                return False
            iterator = iterator.children[c]
        return iterator.word

    def startsWith(self, prefix: str) -> bool:
        iterator = self.root
        for c in prefix:
            if not(c in iterator.children):
                return False
            iterator = iterator.children[c]
        return True
        