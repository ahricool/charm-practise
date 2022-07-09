# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=k
        res=0

        def dfs(ptr):
            nonlocal count,res
            if ptr is None:
                return
            dfs(ptr.left)
            count-=1
            if count==0:
                res=ptr.value
            dfs(ptr.right)
        dfs(root)

        return res