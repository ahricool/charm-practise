"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ids1=[]
        ids2=[]
        p1=head
        p2=dummy=Node(0,None,None)
        while p1 !=None:
            ids1.append(id(p1))
            p2.next=Node(p1.val,None,None)
            ids2.append(p2.next)
            p1=p1.next
            p2=p2.next

        p1=head
        p2=dummy.next
        while p1!=None:
            if p1.random !=None:
                p2.random = ids2[ids1.index(id(p1.random))]
            p1=p1.next
            p2=p2.next

        return dummy.next


        