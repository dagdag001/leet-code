# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = []
        n2 = []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        
        result = str(int(\\.join(map(str, n1[::-1]))) + int(\\.join(map(str, n2[::-1]))))
        result = result[::-1]
        dummy = ListNode(0)

        l3 = dummy
        for _ in result:
            l3.next = ListNode(int(_))
            l3 = l3.next
        return dummy.next
