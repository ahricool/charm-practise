# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur=head
        pre=None
        while cur!=None:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        return pre

