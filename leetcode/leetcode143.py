# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 初值的设置会最终影响你指针停靠的位置是在 左侧 还是 右侧
        # 在此会停靠在左侧
        ptr=head.next
        ptr_mid=head
        while ptr and ptr.next:
            ptr=ptr.next.next
            ptr_mid=ptr_mid.next

        # 逆序第二个链表
        pre,cur=None,ptr_mid.next
        ptr_mid.next=None
        while cur:
            nxt=cur.next
            cur.next,pre,cur=pre,cur,nxt

        # 并归
        cur1,cur2=head,pre
        while cur1.next:
            nxt1=cur1.next
            nxt2=cur2.next
            cur1.next=cur2
            cur2.next=nxt1
            cur1,cur2=nxt1,nxt2

        cur1.next=cur2

        return head

