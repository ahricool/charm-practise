# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 1 and head.next == None:
            return None

        # Dummy 节点是必须要的，不然无法处理删除头节点。
        dummy = ListNode(0, head)
        fast = slow = dummy
        count = 0
        while fast != None:
            fast = fast.next
            if count > n:  # slow 应该指向前一个节点
                slow = slow.next
            count += 1

        slow.next = slow.next.next

        return dummy.next
