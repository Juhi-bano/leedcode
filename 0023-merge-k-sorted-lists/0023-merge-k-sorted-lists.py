# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for list in lists:
            while list:
                result.append(list.val)
                list = list.next
        result.sort()
        dummy = ListNode()
        current = dummy
        for num in result:
            current.next = ListNode(num)
            current = current.next
        return dummy.next
