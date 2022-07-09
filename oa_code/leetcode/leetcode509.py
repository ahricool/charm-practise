# 这种方法本质就是一种动态规划
# 只是把dp矩阵给优化掉了而已


class Solution:
    def fib(self, n: int) -> int:

        if n==0:
            return 0
        if n==1:
            return 1

        pre1,pre2,cur=0,1,1
        for i in range(2,n+1):
            cur=pre1+pre2
            pre1,pre2=pre2,cur

        return cur