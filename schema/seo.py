params={
    "item1":1,
    "item2":2,
    "item3":3,
    "item4":4,
}

def func(a,b,c,item=1):
    print(a,b,c,item)

if __name__=="__main__":
    func(2,3,4,item=1params)