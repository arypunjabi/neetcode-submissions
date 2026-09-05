# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = ListNode()
        carry = 0
        head = sumNode

        while l1 or l2 or carry > 0:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum >= 10:
                carry = 1
            else:
                carry = 0
            sum = sum % 10
            sumNode.val = sum
            if(l1 or l2 or carry > 0):
                sumNode.next = ListNode()
                sumNode = sumNode.next
        return head
            