# [1,2,3,4,5,6]   6   返回


# dp[i][j]  和为j  nums[ 0-i] 的个数

import numpy as np

def sum_counter(nums,target):

    # dp[i][j] nums 0-j 之间和为i的个数
    dp=[[0 for _ in range(len(nums))] for _ in range(target+1)]

    # dp[0][j] nums 0-j 之间和为0的个数
    for j in range(len(dp[0])):
        dp[0][j]=1

    # dp[i][0] nums 0-0 之间和为i的个数
    for i in range(len(dp)):
        if i==nums[0]:
            dp[i][0]=1

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            n=nums[j]
            # select
            if i-n>=0:
                dp[i][j]+=dp[i-n][j-1]
            # not select
            dp[i][j]+=dp[i][j-1]
    # print(np.array(dp))

    return dp[-1][-1]

def sum_counter2(l,target):
    ans=0
    cur=[]


    def count(index):
        nonlocal cur,ans,l
        for i in range(index,len(l)):
            cur.append(l[i])
            s=sum(cur)
            if s==target:
                ans+=1
            elif s<target:
                count(i+1)
            cur.pop()
    count(0)
    return ans

a=[1,2,3,4,5,6]  # 4
print(sum_counter(a,6)) # 4

a=[1,1]
print(sum_counter(a,2)) # 1
print(sum_counter(a,1)) # 2

a=[6,5,4,3,2,1,6,6]
print(sum_counter(a,6))  # 6

a=[6,5,4,3,2,1,6,6,0]
print(sum_counter(a,6))  # 12
