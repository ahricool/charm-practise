
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def build(preorder,inorder):
            if not preorder or not inorder:
                return None

            node=TreeNode(preorder[0])
            inorder_node_index=inorder.index(node.val)

            if 0<inorder_node_index:
                left_lens=inorder_node_index
                node.left=build(preorder[1:left_lens+1],inorder[0:inorder_node_index])

            if inorder_node_index!=len(inorder)-1:
                right_lens=len(inorder)-1-inorder_node_index
                node.right=build(preorder[-1*right_lens:],inorder[-1*right_lens:])
            return node

        return build(preorder,inorder)







