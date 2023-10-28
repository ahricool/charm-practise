# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ptr1 = head
        # 开始的时候  slow 和 fast 的指针所指向的位置要注意一下，
        #  如果 slow,fast=head,head 那么 slow中至少会有两个元素，会无限调用
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ptr2 = slow.next
        slow.next = None

        ptr1 = self.sortList(ptr1)
        ptr2 = self.sortList(ptr2)

        return self.combine(ptr1, ptr2)

    def combine(self, ptr1, ptr2):
        dummy = ListNode()
        ptr = dummy
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next

        if ptr1:
            ptr.next = ptr1
        if ptr2:
            ptr.next = ptr2
        return dummy.next