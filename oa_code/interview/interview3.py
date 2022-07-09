""""
输入数组 只含 0,1

int 数组里面的0 替换1 替换次数

返回整数  最长的连续1的长度
"""


def max_len(nums,k):
    s=0
    prefix=[0]
    for idx in range(len(nums)):
        s+=nums[idx]
        prefix.append(s)
    ans=len(nums)
    while ans>0:
        for idx in range(len(prefix)):
            if idx+ans>=len(prefix):
                break
            if prefix[ans+idx]-prefix[idx]+k>=ans:
                return ans
        ans-=1
    return 0



print(max_len([1,0,1],1))
print(max_len([0,1,0,1],2))
print(max_len([0,0,1,1,0,0,1,1,1,1,1,1,1],2))

""""
输入数组 只含 0,1

int 数组里面的0 替换1 替换次数

返回整数  最长的连续1的长度
"""

# a,b,c,d,e
# [1,2,3,4,5]

def sub_count(nums):
    dp=[0 for _ in range(len(nums))]

    for i in range(2,len(nums)):
        if dp[i-1]==0:
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=1
            else:
                dp[i]=0
        else:
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=0

    return sum(dp)

print(sub_count([1,2,3,4,5,0,1,2,3,4,5]))


from collections import deque

deque.inse



