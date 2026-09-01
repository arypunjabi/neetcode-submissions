class PTreeNode:
    def __init__(self):
        self.children = {}
        self.word = None

class PrefixTree:

    def __init__(self):
        self.root = PTreeNode()

    def insert(self, word: str) -> None:
        iterator = self.root
        for c in word:
            if not(c in iterator.children):
                iterator.children[c] = PTreeNode()
            iterator = iterator.children[c]
        iterator.word = word


    def search(self, word: str):
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
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = PrefixTree()
        valWords = set()
        visit = set()

        for word in words:
            trie.insert(word)
        root = trie.root

        def dfs(node, posR, posC, visit, valWords):
            if posR < 0 or posR >= len(board) or posC < 0 or posC >= len(board[0]) or (posR, posC) in visit or board[posR][posC] not in node.children:
                return
            node = node.children[board[posR][posC]]
            if node.word != None:
                valWords.add(node.word)
            

            visit.add((posR, posC))
            dfs(node, posR + 1, posC, visit, valWords)
            dfs(node, posR - 1, posC, visit, valWords)
            dfs(node, posR, posC + 1, visit, valWords)
            dfs(node, posR, posC - 1, visit, valWords)
            visit.remove((posR, posC))
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(root, r, c, visit, valWords)
        
        return list(valWords)
