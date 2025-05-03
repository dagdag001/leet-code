# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcf(a, b):
            while b:
                a, b = b, a%b
            return a
        prev = head
        temp = head.next
        while temp:
            prev.next = ListNode(gcf(prev.val, temp.val))
            prev.next.next = temp
            prev = temp
            temp = temp.next
        return head
        


