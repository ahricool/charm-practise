from functools import wraps
import functools

functools.lru_cache()

def singleton(cls):
    """单例类装饰器"""

    print("111111")
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        print("222222")
        print(len(instances))
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President:
    pass

@singleton
class President2:
    a="heelo,world"

    pass

President()

President()
President()

President2()
President()
President()
obj=President2()

import pickle # 可以对任意对象进行序列化和反序列化操作

import copy
a=copy.copy(obj)
b=copy.deepcopy(obj)

print(b==obj)
print(b is obj)

# a=pickle.dumps(obj)
# print(a)
#
# b=pickle.loads(a)
# print(b)
#
#
# # 浅拷贝通常只复制对象本身，而深拷贝不仅会复制对象，还会递归的复制对象所关联的对象。
#
