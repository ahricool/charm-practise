# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool: 

        def check(node1,node2):
            if node2 is None:
                return True
            
            if not node1 or node1.val!=node2.val:
                return False

            return  check(node1.left,node2.left) and check(node1.right,node2.right)
        

        def dfs(node):
            if node is None:
                return False
            if check(node,B):
                return True    
            return dfs(node.left) or dfs(node.right)
        
        return dfs(A)
        

