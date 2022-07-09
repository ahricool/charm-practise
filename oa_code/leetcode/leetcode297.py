# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(ptr):
            nonlocal res
            res.append(ptr.val)
            if ptr.left is None:
                res.append(None)
            else:
                dfs(ptr.left)
            if ptr.right is None:
                res.append(None)
            else:
                dfs(ptr.right)

        if root:
            dfs(root)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        res = eval(data)
        print(res)

        def dfs(ptr):
            print(ptr)
            left_value = res.pop(0) if res else None
            print(left_value)
            if left_value is not None:
                ptr.left = TreeNode(left_value)
                dfs(ptr.left)
            right_value = res.pop(0) if res else None
            print(right_value)
            if right_value is not None:
                ptr.right = TreeNode(right_value)
                dfs(ptr.right)

        if res:
            dummy = TreeNode(None)
            dfs(dummy)
            return dummy.left
        else:
            return None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))