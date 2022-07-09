
# 引入 Celery 的 app
from .celery import app


# 创建一个名字为 add 的任务
@app.task
def add(x,y):
    return x+y

# 创建另外三个任务
@app.task
def mul(x,y):
    return x*y

@app.task
def xsum(numbers):
    return sum(numbers)

# 调用任务
result=add.delay(4,4) # add 是任务名
result=add.apply_async((4,4),queue="one",countdown=10) # delay()  是 apply_async() 的快捷调用 apply_async 可以指定更多参数 queue 自定义 队列

# countdown 倒计时 默认是0



# result 是一个 AsyncResult 的实例代表任务执行的结果

result.id # 获取任务id
result.ready() # 检查任务是否完成
result.failed() # 检查任务是否失败
result.successful() # 检查任务是否成功
result.get(timeout=1) # 返回任务结果  任务出现异常 调用 get 会再次引发异常。
result.traceback() # 打印任务异常的tb


### 工作流

# 签名
s1=add.signature((2,2),countdown=10) # 将 add.apply_async((4,4),queue="one",countdown=10) 封装任务调用的参数以及执行选项
res=s1.delay() # 通过签名调用任务
res.get()

# Groups  并行调用任务列表
from celery import group
group(add.s(i,i) for i in range(10))().get()
# res: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Chains 串行调用任务列表

from celery import chain
chain(add.s(4,4)|mul.s(8))().get()
# res: 64

