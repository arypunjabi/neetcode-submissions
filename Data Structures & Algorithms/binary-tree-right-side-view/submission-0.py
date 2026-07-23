# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root:
            queue = deque([[root]])
        else: 
            return []
        returnList = []

        while queue:
            tempList = queue.popleft()
            returnList.append(tempList[len(tempList)-1].val)
            newList = []

            for n in tempList:
                if n.left:
                    newList.append(n.left)
                if n.right:
                    newList.append(n.right)
            if newList:
                queue.append(newList)

        return returnList