class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        square = set()
        
        for i in range(9):
            row = set()
            col = set()
            square = set ()

            for x in range(9):
                if board[i][x] in row and board[i][x] != ".":
                    print("False row at" + str(i) + str(x))
                    return False
                else:
                    row.add(board[i][x])
                
                if board[x][i] in col and board[x][i] != ".":
                    print("False Col")
                    return False
                else:
                    col.add(board[x][i])
            
            sqR = i//3
            sqC = i%3
            for y in range(3):
                for z in range(3):
                    if board[(sqR*3) + y][(sqC * 3) + z] in square and board[(sqR*3) + y][(sqC * 3) + z] != ".":
                        print("false sq")
                        return False
                    else:
                        square.add(board[(sqR*3) + y][(sqC * 3) + z])
            
        return True


