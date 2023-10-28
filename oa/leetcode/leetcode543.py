# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        
        def dfs(root):
            nonlocal d
            if root==None:
                return 0

            l=dfs(root.left)
            r=dfs(root.right)

            d=max(d,l+r)
            return max(l,r)+1
        dfs(root)
        return d
            