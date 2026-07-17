# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        less = p.val if p.val < q.val else q.val
        more = q.val if q.val > p.val else p.val

        while root:
            if less < root.val and more > root.val:
                return root
            elif less < root.val and more < root.val:
                root = root.left
            elif less > root.val and more > root.val:
                root = root.right
            else:
                return root