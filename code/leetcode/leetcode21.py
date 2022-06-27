# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root=head = ListNode()
        ptr1 = l1
        ptr2 = l2
        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                head.next = ptr1
                ptr1=ptr1.next
                head=head.next

            else:
                head.next = ptr2
                ptr2=ptr2.next
                head=head.next

        if ptr1!=None:
            head.next=ptr1
        if ptr2!=None:
            head.next=ptr2
        return root.next
