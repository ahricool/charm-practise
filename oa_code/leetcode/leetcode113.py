# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []

        res=[]
        def dfs(ptr,path):
            path.append(ptr.val)
            if ptr.left is None and ptr.right is None:
                if sum(path)==targetSum:
                    res.append(copy.copy(path))
                    # 复制的也可以用 path[:]

            if ptr.left:
                dfs(ptr.left,path)
            if ptr.right:
                dfs(ptr.right,path)
            path.pop()
        dfs(root,[])
        return res

