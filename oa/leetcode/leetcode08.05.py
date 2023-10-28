


class Solution:
    def multiply(self, A: int, B: int) -> int:
        return A*B

# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 62.92%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 40.46%
# 的用户

import functools

class Solution:

    @functools.lru_cache
    def multiply(self, A: int, B: int) -> int:
        if A<B:
            A,B=B,A

        if B%2==1:
            return self.multiply(A,B-1)+A

        else:
            return self.multiply(A,B//2)+self.multiply(A,B//2)



