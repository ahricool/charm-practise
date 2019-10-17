import re

s = "a/b/c/root/sales-2019-09"

p = re.compile(r"sales-(\d{4}-\d{2})")
match = p.search(s)
print(match.group(0))
print(match.group(1))

def fc(days=8):
    print(days)

if __name__ == "__main__":
    test = open("/Users/huazhang/workspace/CharmTest/regex/regextest.py")
    print(next(test))
    a = ["aa", "b", "c"]
    b = ["aa", "b", "c"]
    print(id(a))
    print(id(b))
    print(a == b)
    a = 1 + 2


    s="sales-12019-01-0000.csv"
    ret=re.compile("^sales-\d{4}-\d{2}-\d*").match(s)

    print(ret)

    #
    # a=["2","1","3"]
    # print(a.index("4"))

    fc()
    fc(2)
