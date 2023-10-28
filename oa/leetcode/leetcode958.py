# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        max_deep=0
        res=True
        def dfs(ptr,deep):
            if ptr is None:
                max_deep=

            dfs(ptr.left,deep+1)
            dfs(ptr.right,deep+1)

        dfs(root,0)
        return res




