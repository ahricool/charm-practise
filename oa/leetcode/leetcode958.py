# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:

        is_end=False

        queue=[root]
        while queue:

            ptr=queue.pop(0)
            
            if ptr !=None:
                if is_end:
                    return False

                queue.append(ptr.left)
                queue.append(ptr.right)
            else:
                is_end=True

        return True




