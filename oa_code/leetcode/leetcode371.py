# 求两数之和，要求不用加法

# 1. 指数 对数运算可以将加法运算转为乘法运算

# 这种方法理论上是可以的，但是用由于计算精度的问题，有些测试例通不过
# math.log 返回的结果是一个 float

# 对于 int 类型 Python 可以表示任意数值（只要你内存够）
# 对于 float 类型 Python 仅可以表示最多17位数字 64位双精度

import math
class Solution:
    def getSum(self, a: int, b: int) -> int:


        return math.log(math.exp(a)*math.exp(b))


# 2. 通过位运算

