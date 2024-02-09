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


# 最清晰的代码，请记住
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        pre=cur=dummy

        counter=0
        while cur.next is not None:
            cur=cur.next
            counter+=1

            if counter%k==0:
                nxt=cur.next
                cur.next=None

                head,rear=self.reverse(pre.next)

                pre.next=head
                rear.next=nxt

                pre=cur=rear

        return dummy.next





    def reverse(self,head):
        pre=None
        cur=head
        while cur !=None:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt

        return pre,head
            







