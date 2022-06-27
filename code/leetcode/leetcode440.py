# 这么写没有问题，就是会超时
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        self.count = 0
        self.res=0

        def dict_num(num):
            if num>n:
                return

            self.count+=1
            if self.count==k:
                self.res=num
                return

            for i in range(10):
                cur_num = num * 10 + i
                dict_num(cur_num)
        for i in range(1,10):
            dict_num(i)
        return self.res


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_prefix(prefix,n):
            count=0
            cur=prefix # 当前前缀
            nxt=prefix+1
            while cur<=n:
                count+=min(nxt,n+1)-cur
                cur *= 10
                nxt *= 10

            return count

        p=1 # 当然选择的数
        prefix=1 # 当前前缀
        while p<k:
           count=get_prefix(prefix,n)  # 在当前前缀下 所有子节点的个数
           if p+count>k:
               prefix*=10
               p+=1
           else:
               prefix+=1
               p+=count

        return prefix


