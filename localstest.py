def hello(**kwargs):
    hi=1
    hello=2
    print(locals())


if __name__=="__main__":
    print(locals())
    hello(info="info",key="56",b="which")
    print(locals())