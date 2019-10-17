class Case:
    def __new__(cls):
        print("__case__new__")
        return super().__new__(cls)

    def __init__(self):
        self.clz="Case"
        print("__case_init__")


class Model:
    def __new__(cls):
        print("__new__")
        return Case.__new__(Case)

    def __init__(self):
        self.clz="Model"
        print("__init__")


m=Model()
print(m)
print(type(Model),type(m))

# print(m.clz)  # 会报错，因为你 new 返回的不是 Model 对象，返回的是Case 对象，两个类 __init__都不会调用

# 实例化的过程分为两个
# 调用 __new__ 生成一个对象, 然后调用 __init__ 来初始化
# 如果你 __new__ 返回的是别的什么东西，那么无论哪个 __init__ 都不会调用

print("-------------------------------")
class Modelx:
    def __new__(cls,*args,**kwargs):
        print(cls,args,kwargs)
        print("__new__")

        cls.static="Static Member"
        cls.func= lambda self,x = "Hello World! ":x
        return super().__new__(cls)

    def __init__(self):
        print("__init__")
        self.clz = "Model"

    def hello(self):
        print("hello")

# print(Modelx.static)  会报错 因为此时还没有运行过 __new__
# print(Modelx.func())
x=Modelx()
print(Modelx.static) # 不会报错 运行过 __new__ 已经在类实例绑定上了 static
# print(Modelx.func()) # 这俩都会报同一个错误，少一个参数
# print(Modelx.hello())
print(x.func()) # 调用实例的就没有问题
