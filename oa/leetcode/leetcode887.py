def hello(i):

    exec("i={};print(i);",{"i":i})
    print(i)

if __name__=="__main__":
    hello(123)