# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 一定要在纸上画一画这个过程，不然你真的做不出来
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1:
            return head

        def reverse(dummy,r):
            nxt=r.next
            pre,cur=None,dummy.next
            while cur!=nxt:
                tmp=cur.next
                cur.next=pre
                pre,cur=cur,tmp
            r=dummy.next
            r.next=cur
            dummy.next=pre
            return r

        dummy=ListNode(0,head)
        pre,cur=dummy,head
        count=1

        while cur.next!=None:
            cur=cur.next
            count+=1
            if count%k==0:
                cur=reverse(pre,cur)
                pre=cur
        return dummy.next





