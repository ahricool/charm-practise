
a=[1,2,3]
b=a
c=b
print(a,b,c)
del a
print(b)

try:
    1/0
except Exception as e:
    print(str(e))


a={"a2":1,"b":2,"c":3,"d":4}
for k,v in a.items():
    a.pop(k)
    print(k,v)