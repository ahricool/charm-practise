# 华为od 2面
# 给定一个m行n列的二维数组，每行只由0，1组成，每行可以左右移动，求解出使得数组出现某一列全为1的最小步数。M，N长度为1~1000。
# array=
# [[1,0,0,0,0,1,0,1],
#  [0,1,0,1,0,0,0,0],
#  [1,0,0,0,0,1,0,1]]

import math
def find_min_step(array):
    m=len(array)
    n=len(array[0])

    min_step=math.inf
    for i in range(n):
        count=0
        for j in range(m):
            if array[j][i]==0:
                l_min=math.inf
                idx=i
                while 0<=idx<n:
                    if array[j][idx] == 0:
                        idx-=1
                    else:
                        l_min=abs(i-idx)
                        break

                r_min=math.inf
                idx=i
                while 0<=idx<n:
                    if array[j][idx] == 0:
                        idx+=1
                    else:
                        r_min=abs(i-idx)
                        break
                count+=min(l_min,r_min)
        min_step=min(min_step,count)

    return min_step

a=[[1,0,0,0,0,1,0,1],
 [0,1,0,1,0,0,0,0],
 [1,0,0,0,0,1,0,1]]

print(find_min_step(a))








