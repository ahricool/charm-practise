# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 16:15

# dfs 遍历
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        ptr=root
        idx=1
        def dfs(ptr,idx):
            if len(res)>=idx:
                if idx%2==1:
                    res[idx-1].append(ptr.val)
                else:
                    res[idx-1].insert(0,ptr.val)
            else:
                res.append([ptr.val,])
            if ptr.left is not None:
                dfs(ptr.left,idx+1)
            if ptr.right is not None:
                dfs(ptr.right,idx+1)

        dfs(ptr,idx)
        return res

# bfs 遍历

