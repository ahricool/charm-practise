"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        if not root:
            return None

        dummy=Node(0)
        self.cur=dummy
        def dfs(ptr):
            if ptr.left is not None:
                dfs(ptr.left)
            print(ptr.val)
            r=ptr.right
            self.cur.right=ptr
            ptr.left=self.cur
            self.cur=ptr
            if r is not None:
                dfs(r)
        dfs(root)

        self.cur.right=dummy.right
        dummy.right.left=self.cur

        return dummy.right
