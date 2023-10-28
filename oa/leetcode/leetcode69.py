# 或者可以用牛顿迭代法 这种方法收敛的更快 

class Solution:
    def mySqrt(self, x: int) -> int:
        # 边界
        if x<=1:
            return x

        left,right=0,x
        while left<=right:
            mid=(right+left)//2
            if mid*mid<x and (mid+1)*(mid+1)>x:
                return mid

            if mid*mid<x:
                left=mid+1
            else:
                right=mid-1

