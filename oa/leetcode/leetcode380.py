class RandomizedSet:

    def __init__(self):
        self.d={}
        self.l=[]


    def insert(self, val: int) -> bool:
        if val not in self.d.keys():
            self.l.append(val)
            self.d[val]=len(self.l)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.d.keys():
            idx=self.d[val]
            last_value=self.l[-1]
            self.l[idx]=last_value
            self.l.pop()
            self.d[last_value]=idx
            self.d.pop(val)
            return True

        return False




    def getRandom(self) -> int:
        """两种 random 的方式 要记住"""
        # import random
        # idx=random.randint(0,len(self.l)-1)
        # return self.l[idx]
        import random
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()