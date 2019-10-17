print("Thanks --1")


class Person:
    print("Hello, Thanks!--2")  # import 这个模块的时候就会执行 其实和写在类外面是一样的

    def __init__(self, name):
        print("__init__")
        self._name = name


print(type(Person("Ahri")))  # 实例是类的对象
print(type(Person))  # 类是 type 的对象
print(type(type))  # type 是 type 自己的对象


class Student1(object):  # 当我们使用 class 关键字的时候，解释器是通过 type函数 来创建 type的对象（也就是类的）所以我们可以通过 type 函数手动实现动态类
    pass


Student2 = type("Student2", (), {})  # 使用 type 函数来手动创建一个类

s1 = Student1()
s2 = Student2()

print(type(Student1), type(Student2))
print(type(s1), type(s2))

# 使用 type 创建带有属性的类，添加的属性是类属性，并不是实例属性
Girl = type("Girl", (), {"country": "china", "sex": "female"})
girl = Girl()
print(girl.country, girl.sex)
print(type(girl), type(Girl))


def speak(self):
    print("normalmethod")


@classmethod
def run(cls):
    print("classmethod")


@staticmethod
def eat():
    print("staticmethod")


# 使用type 创建类，添加静态方法，类方法，普通方法和添加属性差不多
Boy = type("Boy", (), {"speak": speak, "run": run, "eat": eat, "sex": "male"})
boy = Boy()
boy.speak()
boy.eat()
boy.run()
print(boy.sex)
print(type(boy), type(Boy))


class Person(object):
    def __init__(self):
        print("Person")


class Animal(object):
    def __init__(self):
        print("Animal")


# 定义一个子类
Fox = type("Fox", (Person, Animal), {"sex": "Female"})
ahri = Fox()
print(type(ahri), type(Fox))

#     通过type添加的属性是类属性，并不是实例属性
#     通过type可以给类添加普通方法，静态方法，类方法，效果和通过class定义是一样的
#     class创建类的本质就是用type创建。所以可以说python中所有类都是type创建的。

# 元类就是类的类，type 函数就是一个元类。type 是Python 的内建元类，用来创建 Python 中几乎所有的类。也可以创建自己的元类。

# 除了用type 查看对象所属的类，__class__ 熟悉也可以查看。
a = 1
print(a.__class__)
print(a.__class__.__class__)

print(type(object))
print(type(None))

# object 和 type 是从两个不同的角度来对类进行描述的
# object 是从继承的角度
# type 是从类型的角度
# 所有非object类都继承自Object类
# 所有类的类型包括type类都是type
# type类继承自object类，object类的类型也是type类
