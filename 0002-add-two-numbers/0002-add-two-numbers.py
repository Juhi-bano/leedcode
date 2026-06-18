# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        P1 = l1
        P2 = l2
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while P1 or P2 or carry:
            if P1:
                val1 = P1.val
            else:
                val1 = 0
            if P2:
                val2 = P2.val
            else:
                val2 = 0
            Total = val1 + val2 + carry
            carry = Total // 10
            digit = Total % 10
            current.next = ListNode(digit)
            current = current.next
            if P1:
                P1 = P1.next
            if P2:
                P2 = P2.next
        return dummy.next



        