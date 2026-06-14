# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node
        
        p1 = head
        p2 = prev
        result = 0
        while p2:
            curr_sum = p1.val + p2.val
            result = max(result,curr_sum)
            p1 = p1.next 
            p2 = p2.next 
        return result