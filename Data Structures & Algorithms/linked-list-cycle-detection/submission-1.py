# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        currNode = head
        if not currNode:
            return False

        while currNode.next:
            if currNode in visit:
                return True
            visit.add(currNode)
            currNode = currNode.next
        return False