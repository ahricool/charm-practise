# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        d=collections.defaultdict(list)
        def dfs(ptr,depth):
            if not ptr:
                return
            d[depth].append(ptr.val)
            dfs(ptr.left,depth+1)
            dfs(ptr.right,depth+1)

        dfs(root,0)
        ans=[]
        for i in range(len(d)):
            ans.append(d[i])

        return ans



