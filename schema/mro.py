class A:
    def hello(self):
        print("Hello")

class B(A):
    pass

class C:
    def hello(self):
        print("Word")

class D(B,C):
    pass

if __name__=="__main__":
    ins=D()
    ins.hello()
    print(D.__mro__)