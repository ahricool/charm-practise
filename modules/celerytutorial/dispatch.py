from modules.celerytutorial.tasks import add

# result 是 AsyncResult 实例，表示worker的工作结果
result=add.delay(4,4)
"""
这个 task 会被我们之前启动的 work 来处理，我们可以在work的 console 里面看到输出

"""

# ready() 可以检测worker是否完成task
# print(result.ready())

# #
# print(result.get(timeout=1))