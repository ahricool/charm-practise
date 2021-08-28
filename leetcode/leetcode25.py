# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head

        def reverse(h,r):

            pre=r.next
            stop=r.next
            cur=h
            while cur!=stop:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt

        head=pre=ListNode(0,head)
        cur=head.next
        count=0

        while cur.next!=None:
            count+=1
            if count%k==1:
                h=cur
            if count%k==0:
                r=cur
                reverse(h,r)
                pre.next=cur
                pre=h
                cur=h


            cur=cur.next
        return head.next





