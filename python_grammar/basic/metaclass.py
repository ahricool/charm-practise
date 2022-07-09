# 用来生成代码的程序叫做元程序 metaprogram ，编写这种程序就叫元编程 metaprograming

# 自己创建的元类
class ModelMeta(type):
    def __new__(typ, name, bases, attrs: dict):
        print(typ)
        print(name)
        print(bases)
        print(attrs)
        print("-- ModelMeta new --")

        return super().__new__(type, name, bases, attrs)


# 到这里应该更能体会到 __new__和__init__的区别
# __new__ 是用来创建一个实例并返回，而__init__ 是初始化一个实例


# Python 脚本运行到这里不会产生任何输出

# 但是如果要运行到下面，就会打印 ModelMeta 的 __new__ 里面的输出。
# A 类指定了 ModelMeta 作为元类，生成 A类对象，就是生成 ModelMeta 的实例。
# 所以会调用 ModelMeta 里面的 __new__ 方法

class A(metaclass=ModelMeta):  # 使用自己创建的元类
    id = 100

    def __init__(self):
        self.x = 2000


# 因为是继承关系，此时已经有A类对象，生成B类对象，不需要再次生成A类对象
class B(A):
    pass


# C类和A类是一样的，只不过方式不同，这是使用元类的两种方式
C = ModelMeta("C", (), {"parm": 100})


# 元类应用的例子

class ModelMeta(type):
    def __new__(typ, name, bases, attrs: dict):
        print(typ)
        print(name)
        print(bases)
        print(attrs)
        print("-- ModelMeta new --")

        # 使用元类动态注入表名
        # 会自动添加一个 __tablename__ 的属性，值是类名
        tbname = "__tablename__"
        if tbname not in attrs.keys():
            attrs[tbname] = name

        return super().__new__(typ, name, bases, attrs)


class ModelBase(metaclass=ModelMeta):
    def hello(self):
        print("Hello")


print(ModelBase.__tablename__)

# 元编程一般用于框架开发中

print("---------------------------------------")

# 使用元类实现单例模式
# 实例是类的对象，如果实例可以调用，那么需要在类中实现 __call__ 函数
# 类是一个type对象，类的实例化就是对类的调用，那么需要在 type 中实现 __call__ 函数
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        print("__call__")
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    print("hello")
                    cls._instance = super().__call__(*args, **kwargs) # call 中会分别调用 __new__ 和 __init__ 方法。
                    print("thank you")
        return cls._instance


class Foo(metaclass=SingletonType):
    def __new__(cls,name):
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("__init__")
        self.name = name

Foo("Tom")
