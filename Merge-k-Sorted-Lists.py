# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode(0)
            combined = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    combined.next = l1
                    l1 = l1.next
                    
                else:
                    combined.next = l2
                    l2 = l2.next
                combined = combined.next
            combined.next = l1 if l1 else l2
            return dummy.next
        merged = None
        for i in lists:
            merged = merge(merged, i)
        return merged
