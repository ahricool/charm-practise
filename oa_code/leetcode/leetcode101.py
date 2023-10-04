# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(lptr,rptr):
            if lptr is None or rptr is None:
                return lptr==rptr
            
            if lptr.val!=rptr.val:
                return False

            if check(lptr.left,rptr.right) and check(lptr.right,rptr.left):
                return True
            
            return False



        return check(root.left,root.right)
