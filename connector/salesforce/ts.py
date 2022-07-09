class test:
    def __init__(self):
        self.a=123
        self.data={"a":1,
                   "b":2}

    def __getattr__(self,key):
        return self.data[key]


a=test()
print(a.b)