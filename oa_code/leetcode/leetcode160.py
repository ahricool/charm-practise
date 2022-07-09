#
#
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         ptr1,ptr2=headA,headB
#
#         len1,len2=0,0
#         while ptr1 is not None:
#             ptr1=ptr1.next
#             len1+=1
#         while ptr2 is not None:
#             ptr2=ptr2.next
#             len2+=1
#         ptr1,ptr2=headA,headB
#         if len1>len2:
#             for _ in range(len1-len2):
#                 ptr1=ptr1.next
#         if len2>len1:
#             for _ in range(len2-len1):
#                 ptr2=ptr2.next
#
#         while ptr1!=ptr2 and ptr1 is not None:
#             ptr1=ptr1.next
#             ptr2=ptr2.next
#         return ptr1
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr1,ptr2=headA,headB

        while ptr1!=ptr2:
            ptr1=ptr1.next if ptr1 else headB
            ptr2=ptr2.next if ptr2 else headA

        return ptr1