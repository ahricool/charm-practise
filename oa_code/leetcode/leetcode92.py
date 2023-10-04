# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        slow = None
        fast = head

        ptr1 = None
        ptr2 = None

        while fast.next is not None:
            if fast.val == left or fast.val == right:
                if ptr1 is None:
                    ptr1 = slow

                elif ptr2 is None:
                    ptr2 = slow

            slow = fast
            fast = fast.next

        reverse_start = ptr1.next
        reverse_end = ptr2.next.next

        ptr2.next = None

        h1, e1 = self.reverse(reverse_start)
        ptr1.next = h1
        e1.next = reverse_end

        return head

    def reverse(self, head):
        pre = None
        ptr = head

        while ptr is not None:
            nxt = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = nxt

        return pre, head
