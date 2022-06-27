
from celery import Celery

# 第一个参数为当前模块的名称
# 第二个参数为结果后端（用户跟踪任务的状态信息，保存结果，默认是禁用后端的） 这个一般不会用到
# 第三个参数为 broker
# 第四个参数是 任务列表
app=Celery("proj",
           backend='rpc://',
           broker="amqp://",
           include=["celery_tutorial.tasks"])

# 针对 celery 进行配置
app.conf.update(task_serializer="json") # 指定序列化方式

# 路由
# 将任务运行在指定队列中
app.conf.update(task_routes={
    "celery.tasks.add":{"queue":"one"}
})

# 时区 默认的话是 UTC
app.conf.timezone='Europe/London'

"""
启动 worker
celery -A proj worker -l info
-A --app 指定运行 celery 的实例 module.path:attribute 如果只填写包名 会在包内搜索



 -------------- celery@AhriのSpace v5.1.2 (sun-harmonics)
--- ***** -----
-- ******* ---- Windows-10-10.0.19043-SP0 2021-08-28 15:16:13
- *** --- * ---
- ** ---------- [config]
- ** ---------- .> app:         default:0x2bfac419df0 (.default.Loader)
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 16 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery

--concurrency 指定并发度
--queue 设置任务队列  通常用于将任务消息路由到特定的职程（Worker）、提升服务质量、关注点分离、优先级排序的常用手段。

"""

"""
celery inspect  检查运行中的 worker
"""
