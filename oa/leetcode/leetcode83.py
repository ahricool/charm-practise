# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
 
        ptr=head
        while ptr and ptr.next:
            if ptr.next.val== ptr.val:
                ptr.next=ptr.next.next
            ptr=ptr.next
        return head
        
