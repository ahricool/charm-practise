
class A:
    def hello(self):
        print("hello1")

class BMixin:
    def hello(self):
        print("hello2")

class C(A,BMixin):
    s="word"


if __name__=="__main__":
    ins=C()
    ins.hello()

