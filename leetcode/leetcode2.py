# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#  自己纯手写
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = idx = ListNode()
        extra = 0
        while (l1 != None or l2 != None):
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            sum = v1 + v2 + extra
            idx.next = ListNode(sum % 10)
            idx = idx.next
            extra = sum // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if extra != 0:
            idx.next = ListNode(extra)

        return res.next
