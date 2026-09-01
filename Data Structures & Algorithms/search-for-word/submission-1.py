class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def findWord(board, word, visit, posR, posC):
            if posR >= len(board) or posR < 0 or posC >= len(board[0]) or posC < 0 or (posR, posC) in visit or board[posR][posC] != word[0]:
                return False
            else:
                visit.add((posR, posC))
                if len(word) == 1:
                    return True
                else:
                    res = findWord(board, word[1:len(word)], visit, posR + 1, posC) or findWord(board, word[1:len(word)], visit,  posR, posC + 1) or findWord(board, word[1:len(word)], visit, posR - 1, posC) or findWord(board, word[1:len(word)], visit, posR, posC - 1)
                    visit.remove((posR, posC))
                    return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    visit = set()
                    if findWord(board, word, visit, r, c):
                        return True
        
        return False
                