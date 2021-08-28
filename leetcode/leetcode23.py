# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        res=p=ListNode()

        while True:
            head=[l.val if l is not None else None for l in lists]
            cleared_head=list(filter(lambda x: x is not None, head))
            if not cleared_head:
                break
            min_value=min(cleared_head)
            p.next=ListNode(min_value)
            p=p.next
            idx=head.index(min_value)
            lists[idx]=lists[idx].next
        return res.next