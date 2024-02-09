# 链表  头结点   1 ,2 ,3,4,5,6,7,8,None   k=3     1,2，5,4,3,8,7,6

class ListNode:
    def __init__(self,value,nxt):
        self.value=value
        self.next=nxt


def reverse_list(head,k):
    count=0
    cur=head
    while cur:
        count+=1
        cur=cur.next

    n=count%k

    dummy=ListNode(0,head)
    pre=dummy
    cur=dummy
    while n!=0:
        cur=cur.next
        pre=pre.next
        n-=1

    print_list(pre)

    count=0
    while cur.next!=None:

        cur=cur.next
        count+=1

        if count%k==0:

            nxt=cur.next 
            cur.next=None
  
            h,r= reverse(pre.next)

            pre.next=h
            r.next=nxt

            pre=r
            cur=pre
        
    return dummy.next


def reverse(head):
    pre=None
    cur=head
    while cur!=None:
        nxt=cur.next
        cur.next=pre
        pre,cur=cur,nxt

    return pre,head

def print_list(l):
    while l:
        print(l.value)
        l=l.next    

l=ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7,ListNode(8,None))))))))
# print_list(l)
# print_list(reverse(l)[0])
print_list(reverse_list(l,3))