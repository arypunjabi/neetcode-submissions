# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #basically do dfs left aligned because it will automatically find the thing in order
        queue = deque()
        head = root

        def dfs(node):
            if not(node.left or node.right):
                queue.append(node)
                return
            if node.left and not node.right:
                dfs(node.left)                
                queue.append(node)
            if node.right and not node.left:
                queue.append(node)
                dfs(node.right)
            if node.left and node.right:
                dfs(node.left)
                queue.append(node)
                dfs(node.right)
  

        dfs(head)

        for i in range(k):
            res = queue.popleft().val
        
        return res