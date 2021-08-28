# LRU 缓存机制

# # 用List模拟
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cache = {}
#         self.size = capacity
#         self.timeout = []
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.timeout.remove(key)
#             self.timeout.append(key)
#             return self.cache[key]
#         else:
#             return -1
#
#     def sdsd(self):
#         pass
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.timeout.remove(key)
#             self.timeout.append(key)
#         else:
#             if len(self.cache) >= self.size:
#                 timeout_key = self.timeout.pop(0)
#                 self.cache.pop(timeout_key)
#                 self.timeout.append(key)
#                 self.cache[key] = value
#             else:
#                 self.timeout.append(key)
#                 self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DoubleLinkedNode:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self,capacity):
        self.cache=dict()
        self.head=DoubleLinkedNode()
        self.tail=DoubleLinkedNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.size=0

    def get(self,key):
        if key in self.cache:
            ptr=self.cache[key]