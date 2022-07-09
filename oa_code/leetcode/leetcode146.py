# LRU 缓存机制

# 用List模拟
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.timeout = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.timeout.remove(key)  # 这个操作不是o(1)的操作
            self.timeout.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.timeout.remove(key)
            self.timeout.append(key)
        else:
            if len(self.cache) >= self.size:
                timeout_key = self.timeout.pop(0)
                self.cache.pop(timeout_key)
                self.timeout.append(key)
                self.cache[key] = value
            else:
                self.timeout.append(key)
                self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DoubleLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.max_size = capacity
        self.size = 0
        self.data = DoubleLinkedNode()
        self.data.prev = self.data
        self.data.next = self.data
        self.index = {}

    def get(self, key: int) -> int:
        if key in self.index.keys():
            node = self.index[key]
            value = node.value
            self.removeNode(node)
            self.addToEnd(node)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.index.keys():
            node = DoubleLinkedNode(key, value)
            self.addToEnd(node)
            self.index[key] = node
            self.size += 1

            if self.size > self.max_size:
                node = self.data.next
                node.next.prev = self.data  #  node.next.prev
                self.data.next = node.next
                self.index.pop(node.key)
                self.size-=1

        else:
            node = self.index[key]
            node.value = value
            self.removeNode(node)
            self.addToEnd(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToEnd(self, node):
        node.prev = self.data.prev
        node.next = self.data
        self.data.prev.next = node
        self.data.prev = node

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
