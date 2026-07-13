class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L1 = 0
        L2 = 0
        R1 = len(matrix)-1
        R2 = len(matrix[0])-1

        while L1 < R1:
            mid = (L1 + R1)//2
            if target < matrix[mid][0]:
                R1 = mid-1
            elif target > matrix[mid][0] and target > matrix[mid][len(matrix[0])-1]:
                L1 = mid + 1
            else: 
                L1 = mid
                break
        print(L1)
        
        while L2 <= R2:
            mid = (L2 + R2)//2
            if target < matrix[L1][mid]:
                R2 = mid-1
            elif target > matrix[L1][mid]:
                L2 = mid+1
            else:
                return True
            print(L2)
            print(R2)
        
        return False

