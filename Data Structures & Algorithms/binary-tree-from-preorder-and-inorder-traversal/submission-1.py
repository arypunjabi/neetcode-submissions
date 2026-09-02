# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderIndex = {
            value: index
            for index, value in enumerate(inorder)
        }

        def dfs(preLeft, inLeft, inRight):
            if inLeft > inRight:
                return None
            rootValue = preorder[preLeft]
            indexRoot = inorderIndex[rootValue]

            node = TreeNode(preorder[preLeft])
            node.left = dfs(preLeft + 1, inLeft, indexRoot - 1)
            node.right = dfs(preLeft + (indexRoot-inLeft) + 1, indexRoot + 1, inRight)
            return node
         
        head = dfs(0, 0, len(inorder) - 1)
        return head