# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(ptr,value):
            if not ptr:
                return False
            if not ptr.left and not ptr.right and ptr.val==value:
                return True
            else:
                return dfs(ptr.left,value-ptr.val) or dfs(ptr.right,value-ptr.val)

        return dfs(root,targetSum)
