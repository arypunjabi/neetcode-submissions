# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueP = deque()
        queueQ = deque()

        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False

        queueP.append(p)
        queueQ.append(q)

        while queueP and queueQ:
            nodeP = queueP.popleft()
            nodeQ = queueQ.popleft()
            
            if nodeP.val != nodeQ.val:
                return False
            
            if nodeP.left and nodeQ.left:
                queueP.append(nodeP.left)
                queueQ.append(nodeQ.left)
            elif nodeP.left or nodeQ.left:
                return False
            if nodeP.right and nodeQ.right:
                queueP.append(nodeP.right)
                queueQ.append(nodeQ.right)
            elif nodeP.right or nodeQ.right:
                return False
            
        return True
            

        
        