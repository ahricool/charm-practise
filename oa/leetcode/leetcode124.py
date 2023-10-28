# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_val=root.val


        def dfs(ptr):
            l_max_value = dfs(ptr.left) if ptr.left else 0
            r_max_value = dfs(ptr.right) if ptr.right else 0
            ret=max([ptr.val, l_max_value + ptr.val, r_max_value + ptr.val])
            self.max_val=max([self.max_val,ret,l_max_value + ptr.val+r_max_value])
            return max([ptr.val, l_max_value + ptr.val, r_max_value + ptr.val])

        dfs(root)
        return self.max_val