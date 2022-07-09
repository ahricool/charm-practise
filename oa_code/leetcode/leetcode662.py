# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        self.left_side = []
        self.right_side = []

        def dfs(self, ptr, depth, location):
            if ptr:
                if len(self.left_side) <= depth:
                    self.left_side.append(location)
                    self.right_side.append(location)
                else:
                    self.right_side[depth] = location

                dfs(self, ptr.left, depth + 1, 2 * location - 1)
                dfs(self, ptr.right, depth + 1, 2 * location)

        dfs(self, root, 0, 1)

        return max(map(lambda x: x[1] - x[0] + 1, zip(self.left_side, self.right_side)))
