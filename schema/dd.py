# import random
# ss=0
# def aa():
#     global ss
#     ss+=1
#     return ss
# a=[1,2,3,4]
# b=[2,3,4,5]
# c={i:aa() for i in a+b}
# print(c)
# class NewException(Exception):
#     pass
#
# import traceback
#
# try:
#     1/0
#
# except ZeroDivisionError as e:
#     print("Thank you.")
# except Exception as e :
#     aa=traceback.format_exc()
#     print(aa)
#     print("Very much")

_list = []
for i in range(3):
    def func(i):
        def f_closure(a):  # <<<---
            return i + a

        return f_closure


    _list.append(func(i))  # <<<---

for f in _list:
    print(f(1))

import datetime
latest_date=datetime.datetime(2019,10,12)
a= latest_date and latest_date.strftime('%Y-%m-%d')
print(type(a))
print(a)

a={"as":1}
_list=[]
for i in range(10):
    a["as"]=i
    _list.append(a)

print(_list)