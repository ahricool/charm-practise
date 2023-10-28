# 将0元素移到一边，并不改变其他元素的相对顺序。

def sort(l):
    first=second=len(l)-1
    while first>=0 and l[first]!=0:
        first-=1
        second-=1


    print(first,second)
    while first>=0:
        if l[first]!=0:
            l[first],l[second]=l[second],l[first]
            second-=1
        first-=1

    return l

print(sort([0, 1, 0, -1, 0, 3, 0, 6]))
print(sort([0, 1, 0, -1, 0, 3, 0, 0]))
print(sort([1, 2, 3, -1, 4, 3, 5, 6]))
print(sort([0, 0, 0, 0, 0, 0, 0, 0]))
print(sort([999, -2, -3, -1, -4, -3, -5, 0]))
print(sort([0,0,0,1,1,0,0,0]))