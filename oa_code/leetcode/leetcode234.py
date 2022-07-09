# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast=head.next
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        ptr=slow.next
        slow.next=None
        pre_ptr=None
        while ptr:
            nxt=ptr.next
            ptr.next=pre_ptr
            pre_ptr=ptr
            ptr=nxt

        ptr1=head
        ptr2=pre_ptr
        while ptr2:
            if ptr2.val==ptr1:
                ptr1=ptr1.next
                ptr2=ptr2.next
            else:
                return False
        return True



