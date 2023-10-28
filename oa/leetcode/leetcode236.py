# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.search_stack = []
        self.found_count = 0
        self.res = None

        def dfs(ptr):
            if self.found_count == 2:
                return

            appended_stack = False
            if self.found_count == 0:
                appended_stack = True
                self.search_stack.append(ptr)

            if ptr.val == p.val or ptr.val == q.val:
                self.found_count += 1

            if self.found_count == 2:
                self.res = self.search_stack[-1]

            if ptr.left is not None:
                dfs(ptr.left)
            if ptr.right is not None:
                dfs(ptr.right)
            if appended_stack:
                self.search_stack.pop()

        dfs(root)
        return self.res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(ptr):
            if ptr is None:
                return False

            lson= dfs(ptr.left)
            rson= dfs(ptr.right)

            count=0
            if ptr.val==p or ptr.val==q:
                count+=1



        