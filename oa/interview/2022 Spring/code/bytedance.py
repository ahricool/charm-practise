# 字节的多次面试

# 2分搜索树 证明
import math


def two_tree(root):
    ans = True

    def dfs(ptr, min_value, max_value):
        nonlocal ans
        if ptr is None:
            return
        if min_value < ptr.val < max_value:
            dfs(ptr.left, min_value, ptr.val)
            dfs(ptr.right, ptr.val, max_value)
        else:
            ans = False

    dfs(root, -math.inf, math.inf)
    return ans


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# cache API  最大1000
# LRU Cache

# 双端链表
# dict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, size):
        self.size = size
        self.cur_size = 0
        self.d = {}
        self.dummy = Node(None, None)
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy

    def get(self, key):
        if key in self.d.keys():
            node = self.d[key]
            self.removeNode(node)
            self.appendNode(node)
            return node.val
        return None

    def put(self, key, value):
        if key in self.d.keys():
            node = self.d[key]
            node.val = value
            self.removeNode(node)
            self.appendNode(node)
        else:
            node = Node(key, value)
            self.d[key] = node
            self.appendNode(node)
            self.cur_size += 1
            if self.cur_size > self.size:
                self.remove()

    def remove(self):
        node = self.dummy.next
        self.removeNode(node)
        self.d.pop(node.key)
        self.cur_size -= 1

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def appendNode(self, node):
        node.pre = self.dummy.pre
        node.next = self.dummy
        node.pre.next = node
        node.next.pre = node
