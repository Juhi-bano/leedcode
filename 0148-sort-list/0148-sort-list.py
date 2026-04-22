# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
def GetMidd(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    
def merge_sort(head):
    if not head or not head.next:
        return head
    mid = GetMidd(head)
    mid_to_mid = mid.next
    mid.next = None
    left = merge_sort(head)
    right = merge_sort(mid_to_mid)
    sorted_list = merge_two_list(left,right)
    return sorted_list

def merge_two_list(list1:optional[ListNode],list2:optional[ListNode])->optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    if list1 is not None:
        tail.next = list1
    elif list2 is not None:
        tail.next = list2
    return dummy.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)
        
        