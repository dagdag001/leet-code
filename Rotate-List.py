# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def pop(ll):
            temp = ll
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            if prev:
                prev.next = None
            return temp
        def unshift(value: ListNode, ll: ListNode):
            value.next = ll
            
            return value
        
        if not head or not head.next:
            return head 

        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next
        
        
        k = k % length
        if k == 0:
            return head 
        
        for i in range(k):
            head = unshift(pop(head), head)
        return head
            
            