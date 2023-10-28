# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if self.length(l1)<self.length(l2):
            l1,l2=l2,l1

        l1=self.reverse(l1)
        l2=self.reverse(l2)

        p1=l1
        p2=l2

        carry=0
        while p1 is not None or p2 is not None:
            v1=p1.val if p1 is not None else 0
            v2=p2.val if p2 is not None else 0
            value=v1+v2+carry
            carry,p1.val=value//10,value%10
            if p1 is not None:
                p1=p1.next
            if p2 is not None:
                p2=p2.next

        l1=self.reverse(l1)
        if carry !=0:
            c_node=ListNode()
            c_node.next=l1
            c_node.val=carry
            l1=c_node
        return l1



    def reverse(self,l):
        pre=None
        ptr=l
        while ptr is not None:
            nxt=ptr.next
            ptr.next=pre
            pre=ptr
            ptr=nxt
        return pre

    def length(self,l):
        count=0
        while l is not None:
            count+=1
            l=l.next
        return count
