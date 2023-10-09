# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        # 翻转的题目要做dummy
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy.next

        ptr1 = None
        ptr2 = None

        count = 1
        while fast is not None:
            if count == left or count == right:
                if ptr1 is None:
                    ptr1 = slow
                else:
                    ptr2 = slow

            count += 1
            fast = fast.next
            slow = slow.next

        print(head, left, right)
        print(ptr1, ptr2)
        self.reverse(ptr1, ptr2.next)

        return dummy.next

    def reverse(self, pre_head, rear):

        pre = pre_head
        ptr = pre.next
        sentry = rear.next
        # 因为在翻转过程中  rear.next 可能会被改写， 所以要独立保存变量， 不要用 X.next 做条件。
        while ptr != sentry:
            nxt = ptr.next
            ptr.next = pre
            pre = ptr
            ptr = nxt

        pre_head.next.next = ptr
        pre_head.next = pre






def print_list(new_head):
    while new_head is not None:
        print(new_head.val)
        new_head=new_head.next

def partition_reverse(head,k):
    dummy=Node(0,head)
    count=1

    ptr1=dummy
    ptr2=dummy.next
    while ptr2 is not None:
        if count%k==0:
            print(ptr1.val,ptr2.val)
            ptr1=do_reverse(ptr1,ptr2)
            ptr2=ptr1

        count+=1
        ptr2=ptr2.next
    
    return dummy.next
        

def do_reverse(pre_head,rear):
    new_rear=pre_head.next

    pre=pre_head
    ptr=pre_head.next

    #print_list(pre_head)


    end=rear.next

    while ptr != end:
        nxt=ptr.next
        ptr.next=pre
        pre,ptr=ptr,nxt

    pre_head.next=pre
    new_rear.next=ptr
    return new_rear



def reverse(head):
    pre=None
    ptr=head

    while ptr is not None:
        nxt=ptr.next
        ptr.next=pre
        pre,ptr=ptr,nxt

    return pre
    

class Node:
    def __init__(self,value,nxt):
        self.val=value
        self.next=nxt

head=Node(1,Node(2,Node(3,None)))
new_head=reverse(head)


# while new_head is not None:
#     print(new_head.val)
#     new_head=new_head.next



head=Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10,Node(11,None)))))))))))
new_head=partition_reverse(head,3)
print_list(new_head)
