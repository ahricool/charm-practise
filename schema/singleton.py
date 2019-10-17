import threading
class Singleton(object):

    _instance_lock=threading.Lock()
    def __init__(self):
        import time
        time.sleep(1)
        pass


    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with cls._instance_lock:
                if not hasattr(Singleton,"_instance"):
                    Singleton._instance=super().__new__(cls,*args,**kwargs)


        return Singleton._instance

def task(arg):
    obj=Singleton()
    print(obj)

for i in range(10):
    t=threading.Thread(target=task,args=[i,])
    t.start()

