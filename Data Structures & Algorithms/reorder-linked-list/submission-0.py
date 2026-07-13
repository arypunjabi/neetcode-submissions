# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        prev = None
        curr = l2

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        l2 = prev
        
        while l2:
            next1 = l1.next
            next2 = l2.next

            l1.next = l2
            l2.next = next1

            l1 = next1
            l2 = next2


            
