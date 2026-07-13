# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            return self.recurseList(head)
        else:
            return head
    def recurseList(self, head: ListNode) -> ListNode:
        if not(head.next):
            return head
        else:
            reverseRest = self.recurseList(head.next)
            head.next.next = head
            head.next = None
            return reverseRest
            
