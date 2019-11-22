
# 默认的情况下 pytest 只能识别以 test_ 开头 和 _test 结尾的 .py 文件
# 识别以 test 开头的函数、类

# 也可以显示运行 pytest test_work.py

def test_add():
    x=3
    y=4
    assert x==y,"test fialed"


if __name__=="__main__":
    import datetime
    dt=datetime.datetime.now()
    d=datetime.datetime.strptime("0001-01-01","%Y-%m-%d")
    print(d)
    print(dt)
    print(dt.toordinal())
    print((dt-d).days)

    d={"hello":123}
    print(id(d))
    d.clear()
    print(id(d))
    dimensions={
        "hello":1,
        "thank":2
    }
    for dim in dimensions:
        print(dim)
        print(type(dim))
    key = {dim: dimensions[dim] for dim in dimensions}
    print(key)

    t=("q","w")
    print(t[1],t[0])