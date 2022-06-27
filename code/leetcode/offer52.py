# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 这种写法很巧妙，而且速度也很快 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#
#         len1,len2=0,0
#         ptr1,ptr2=headA,headB
#         while ptr1!=None:
#             len1+=1
#             ptr1=ptr1.next
#         while ptr2!=None:
#             len2+=1
#             ptr2=ptr2.next
#
#         ptr1,ptr2=headA,headB
#
#         if len1>len2:
#             for _ in range(len1-len2):
#                 ptr1=ptr1.next
#         else:
#             for _ in range(len2-len1):
#                 ptr2=ptr2.next
#
#         while ptr1:
#             if ptr1==ptr2:
#                 return ptr1.val
#             else:
#                 ptr1=ptr1.next
#                 ptr2=ptr2.next
#
