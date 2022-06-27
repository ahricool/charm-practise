# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        ans=True

        def dfs(ptr):
            nonlocal ans
            if ptr is None:
                return 0

            lh=dfs(ptr.right)
            rh=dfs(ptr.right)

            if abs(lh-rh)>1:
                ans=False
            return max(lh,rh)+1

        dfs(root)
        return ans

