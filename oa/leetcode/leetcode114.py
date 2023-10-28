# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ptr = root
        if root is None:
            return None

        def dfs(node):
            right_node = node.right
            left_node = node.left

            if left_node is not None:
                self.ptr.right = left_node
                self.ptr = self.ptr.right
                dfs(left_node)
            if right_node is not None:
                self.ptr.right = right_node
                self.ptr = self.ptr.right
                dfs(right_node)
            node.left = None

        dfs(self.ptr)
        return root
