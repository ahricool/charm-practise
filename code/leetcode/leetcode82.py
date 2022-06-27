# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head=ListNode(None,head)
        pre_ptr=dummy_head
        ptr=dummy_head.next
        target= None
        while ptr:
            if ptr.next and ptr.val==ptr.next.val:
                target=ptr.val
                ptr=ptr.next
                pre_ptr.next=ptr
            elif ptr.val==target:
                ptr=ptr.next
                pre_ptr.next=ptr
            else:
                ptr=ptr.next
                pre_ptr=pre_ptr.next
        return dummy_head.next

