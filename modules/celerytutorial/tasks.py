from celery import Celery

# 第一个参数是 模块名
# 第二个参数是 broker
app= Celery("tasks",broker="redis://localhost")

@app.task
def add(x,y):
    return x+y

