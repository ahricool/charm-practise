# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        while len(lists)>1:
            new_list=self.merge(lists.pop(0),lists.pop(0))
            lists.append(new_list)
        return lists[0]

    def merge(self,ptr1,ptr2):
        dummy=cur=ListNode()
        while ptr1 and ptr2:
            if ptr1.val<=ptr2.val:
                cur.next=ptr1
                ptr1=ptr1.next
            else:
                cur.next=ptr2
                ptr2=ptr2.next
            cur=cur.next

        if ptr1:
            cur.next=ptr1

        if ptr2:
            cur.next=ptr2

        return dummy.next