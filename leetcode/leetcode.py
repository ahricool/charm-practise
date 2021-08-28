# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(ptr, val):

            val = val * 10 + ptr.val

            if ptr.left:
                dfs(ptr.left, val)
            if ptr.right:
                dfs(ptr.right, val)
            if not ptr.left and not ptr.right:
                self.res += val

        dfs(root, 0)
        return self.res
