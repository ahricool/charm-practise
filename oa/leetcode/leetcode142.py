# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow=head
        fast=head.next
        while fast and fast.next:
            if fast==slow: # 相遇
                p1=head
                count=0
                while p1!=slow:
                    p1=p1.next
                    slow=slow.next

                return count

            else:
                fast=fast.next.next
                slow=slow.next

        return None