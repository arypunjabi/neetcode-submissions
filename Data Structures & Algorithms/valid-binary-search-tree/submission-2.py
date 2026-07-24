# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        dfsStack = [(root, -1001, 1001)]

        while dfsStack:
            tempNode, leftLim, rightLim = dfsStack.pop()

            if not(tempNode.val > leftLim and tempNode.val < rightLim):
                return False
            
            if tempNode.left:
                dfsStack.append((tempNode.left, leftLim, tempNode.val))
            if tempNode.right:
                dfsStack.append((tempNode.right, tempNode.val, rightLim))
        
        return True