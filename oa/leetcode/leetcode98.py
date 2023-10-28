# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans=True

        def dfs(ptr,min_value,max_value):
            nonlocal ans
            if min_value<ptr.val<max_value:
                if ptr.left is not None:
                    dfs(ptr.left,min_value,ptr.val)
                if ptr.right is not None:
                    dfs(ptr.right,ptr.val,max_value)
            else:
                ans=False

        dfs(root,-math.inf,math.inf)
        return ans


