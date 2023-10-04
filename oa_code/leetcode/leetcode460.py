class LFUCache:

    def __init__(self, capacity: int):
        self.max_size=capacity
        self.current_size=0
        self.data={}
        self.count={}
        self.keys=[]


    def get(self, key: int) -> int:
        if key in self.data.keys():
            self.count[key]+=1
            return self.data[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.data.keys():
            self.count[key]+=1
            self.data[key]=value
        else:
            if self.current_size<self.max_size:
                self.current_size+=1
                self.data[key]=value
                self.count[key]+=1
            else:






# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

