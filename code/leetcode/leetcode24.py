# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 主要是需要处理一个前置节点的问题，并且在头节点之前加一个 dummy节点。

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy=ListNode(next=head)
        ptr=dummy
        while ptr!=None and ptr.next!=None and ptr.next.next!=None:
            first,second=ptr.next,ptr.next.next
            first.next=second.next
            second.next=first
            ptr.next=second
            ptr=ptr.next.next

        return dummy.next