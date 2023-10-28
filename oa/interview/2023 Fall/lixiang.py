# 理想汽车1面 

#  数组 正整数 寻找子数字和为 target=10

import copy

def find_sum(array, target):
    ans=[]
    cur=[]
    def finder(idx, total):
        if total == target:
            ans.append(copy.copy(cur))
            return
        if total> target:
            return

        if total< target and idx <len(array):
            for i in range(idx,len(array)):
                cur.append(array[i])
                finder(i+1, total+array[i])
                cur.pop()
    
    finder(0,0)
    return ans
    
a=[1,2,3,4,5]
target=6

print(find_sum(a,target))

