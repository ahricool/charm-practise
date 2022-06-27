class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res=res^i
        return res

# Python 的位运算符
# & 与 | 或 ^ 异或 ~取反 <<左移 >>右移
