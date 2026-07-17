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
        node = root

        while node:
            if less < node.val and more > node.val:
                return node
            elif less < node.val and more < node.val:
                node = node.left
            elif less > node.val and more > node.val:
                node = node.right
            else:
                return node