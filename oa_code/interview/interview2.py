

# o冒泡  o n2

# 堆排序 o nlogn

# 二分排序  o nlogn

# Timsort < o nlogn

# 桶排序  logn 需要其他空间辅助
import math

#
def popsort(l):

    while True:
        cur=0
        f=False
        for idx in range(1,len(l)):
            if l[cur]>l[idx]:
                l[idx],l[cur]=l[cur],l[idx]
                f=True
            cur=idx
        print(l)
        if f is False:
            break
    return l




print(popsort([11,6,4,5,6,2,7]))

#
#
# class Node:
#     def __init__(self,v):
#         self.v=v
#         self.next=None
#
#
def revert_node(ptr):

    cur=ptr
    pre=None
    while cur is not None:
        n=cur.next
        cur.next=pre
        pre=cur
        cur=n

    return pre
#
# # 1,2,3,4
# # pre->1,cur->2, n->3  pre->2 cur->3   pre=4 ->None
#
# switch OS sonic
#

