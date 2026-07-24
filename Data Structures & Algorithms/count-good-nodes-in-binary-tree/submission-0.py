# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        dfsStack = [(root, root.val)]
        numGood = 0

        while dfsStack:
            tempNode, currMax = dfsStack.pop()
            if currMax <= tempNode.val:
                numGood = numGood + 1
                currMax = tempNode.val
            if tempNode.left:
                dfsStack.append((tempNode.left, currMax))
            if tempNode.right:
                dfsStack.append((tempNode.right, currMax))
            

        
        return numGood