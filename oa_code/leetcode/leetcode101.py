# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(lptr,rptr):


            if lptr.val!=rptr.val:
                return False

            if not check(lptr.lrft,lptr.right):
