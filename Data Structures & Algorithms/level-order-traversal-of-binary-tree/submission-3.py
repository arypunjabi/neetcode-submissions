# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = deque([[root]])
        else: 
            return []
        returnList = []

        while queue:
            tempList = queue.popleft()
            returnList.append([node.val for node in tempList])
            newList = []

            for n in tempList:
                if n.left:
                    newList.append(n.left)
                if n.right:
                    newList.append(n.right)
            if newList:
                queue.append(newList)

        return returnList